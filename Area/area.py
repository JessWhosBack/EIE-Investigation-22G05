# EIE Investigation: "Which Hand?"
# Jesse van der Merwe (1829172) and Robyn Gebbie (2127777)
# ELEN4012A 2022

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# COPYRIGHT NOTICE: 
# This code contains snippets from XX article "XX" (XX/XX/XXXX) 
# Which can be found at: https://X
# 
# It has further been modified and combined to suit the needs of this project.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# IMPORTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import cv2
import glob
import os	
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import trapz
import math
from enum import Enum
import pandas as pd
from IPython.display import display
from sympy import false

class Results(Enum):
    FILENAME = 0

    AREA_TRAPZ = 1
    MIN = 2
    Q1 = 3
    Q2 = 4
    Q3 = 5
    MAX = 6
    IQR = 7
    STDDEV = 8

    AVG_AREA_TRAPZ = 9
    AVG_AREA_MIN = 10
    AVG_AREA_Q1 = 11
    AVG_AREA_Q2 = 12
    AVG_AREA_Q3 = 13
    AVG_AREA_MAX = 14
    AVG_AREA_IQR = 15
    AVG_AREA_STDDEV = 16
    
# Read in the .jpgs and save into an image array, ensuring grayscale- - - - - - - - - - - - - - - - - - - - - - - - - - - #
image_array = []
image_names = []
file_count = 0
for filename in glob.glob('Area\Data\*.jpg'):
    im = Image.open(filename).convert('L') # convert image to grayscale
    res = im.point((lambda p: 256 if p>=200 else 0)) # convert each pixel into either black or white
    res.save(filename)

    arrayName = os.path.basename(filename)
    arrayName = arrayName.replace(".jpg","")
    image = cv2.imread(filename)
    image_array.append(image)
    image_names.append(arrayName)
    file_count = file_count + 1

figure_area = plt.figure(0, figsize=(8,10))
figure_area = plt.title("Area")
results_array = [[-1 for x in range(len(Results))] for y in range(file_count)] 

# Loop through the image array to perform image processing- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
for image_counter, image in enumerate(image_array):
    results_array[image_counter][Results.FILENAME.value] = image_names[image_counter]

    # IMAGE PROCESSING TO GENERATE GRAPH OF HAND DRAWN LINE THAT HAS BEEN SHIFTED DOWN TO THE X-AXIS- - - - - - - - - - - #
    # NOTE: The horizontal axis is denoted by y, and the vertical axis is denoted by x (no, this was not on purpose)
    coordinates = np.argwhere(image < 0.9)
    x_tuple, y_tuple, z_tuple = zip(*coordinates)

    x = np.array(x_tuple).tolist()
    y = np.array(y_tuple).tolist()
    z = np.array(z_tuple).tolist()

    average_x = np.mean(x)  
    new_array_x = []
    new_array_y = []
    average_array_x = []
    
    # Sort the array of pixels into an ordered array according to the horizontal x-axis
    for i in range(0, len(y)-1):
        for j in range(0, len(y)-i-1):
            if y[j] > y[j+1]:
                temp_x = x[j]
                x[j] = x[j+1]
                x[j+1] = temp_x

                temp_y = y[j]
                y[j] = y[j+1]
                y[j+1] = temp_y

    # Take the absolute value and shift the points down to be centered around the vertical axis
    for i in range(0, len(x)):
        new_array_y.append(y[i])
        average_array_x.append(0)
        if x[i] < average_x: 
            c = 3
            new_array_x.append(average_x - x[i])
        else:
            new_array_x.append(x[i] - average_x)

    # NOTE: The below code does NOT work as intended - it removes the top X% of all graphs, even those without erroneous border lines
    # Need to try think of better solution! 
    #
    # # Remove erroneous X% of top pixels of image to get rid of any remaining border
    # max_new_x = np.max(new_array_x)
    # x_adjustment = 1/100*max_new_x
    # tracker = 0
    # for i in range(0, len(new_array_x)): 
    #     if new_array_x[tracker] > max_new_x - x_adjustment:
    #         new_array_y.pop(tracker)
    #         new_array_x.pop(tracker)
    #         tracker = tracker - 1
    #     tracker = tracker + 1

    # Plot the shifted points as a line graph 
    figure_area = plt.subplot(math.ceil(file_count/2), 2, image_counter+1)
    figure_area = plt.title(str(image_names[image_counter]))  
    figure_area = plt.plot(new_array_y, new_array_x)
    figure_area = plt.fill_between(new_array_y, new_array_x, color="grey")
    figure_area = plt.xlim(0, 600)
    figure_area = plt.ylim(0, 20)

    # EXTRACTING OF NUMERICAL DATA FROM THE ABOVE GRAPH - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # Area under the curve, using numpy's trapz formula
    total_area_trapz_x = round(trapz(new_array_x), 2)
    results_array[image_counter][Results.AREA_TRAPZ.value] = round(total_area_trapz_x, 2)
    figure_area = plt.text(400, 15, "Area: " + str(total_area_trapz_x), bbox=dict(facecolor='red', alpha=0.5))

    # Quantile values of the data
    min, q1, q2, q3, max = np.quantile(new_array_x, [0, 0.25, 0.5, 0.75, 1])
    iqr = q3-q1
    std = np.std(new_array_x)
    # figure_area = plt.text(400, 10, "Q75: " + str(round(q3, 2)), bbox=dict(facecolor='red', alpha=0.5))
    # figure_area = plt.text(400, 5, "IQR: " + str(round(iqr, 2)), bbox=dict(facecolor='red', alpha=0.5))

    results_array[image_counter][Results.MIN.value] = round(min, 2)
    results_array[image_counter][Results.Q1.value] = round(q1, 2)
    results_array[image_counter][Results.Q2.value] = round(q2, 2)
    results_array[image_counter][Results.Q3.value] = round(q3, 2)
    results_array[image_counter][Results.MAX.value] = round(max, 2)
    results_array[image_counter][Results.IQR.value] = round(iqr, 2)
    results_array[image_counter][Results.STDDEV.value] = round(std, 2)

    average_areas = []
    temp_counter = 1
    max_new_array_y = np.max(new_array_y)
    percent_of_xaxis = int(5/100*max_new_array_y)
    array_iterator = 0
    
    for i in range(percent_of_xaxis, max_new_array_y, percent_of_xaxis):
        temp_array_x = []
        temp_array_y = []
        before_array_iterator = array_iterator

        while new_array_y[array_iterator] < i:
            temp_array_x.append(new_array_x[array_iterator])
            temp_array_y.append(new_array_y[array_iterator])
            array_iterator = array_iterator + 1

        if array_iterator == before_array_iterator:
            temp_array_x.append(new_array_x[array_iterator-1])
            temp_array_y.append(new_array_y[array_iterator-1])
            temp_array_x.append(new_array_x[array_iterator])
            temp_array_y.append(new_array_y[array_iterator])
                     
        temp_area_x = round(trapz(temp_array_x, temp_array_y), 2)
        average_areas.append(temp_area_x)   
        temp_counter = temp_counter + 1

    # Quantile values of the data
    avg_avg_area = np.mean(average_areas)
    avg_min, avg_q1, avg_q2, avg_q3, avg_max = np.quantile(average_areas, [0, 0.25, 0.5, 0.75, 1])
    avg_iqr = avg_q3-avg_q1
    avg_std = np.std(average_areas)

    results_array[image_counter][Results.AVG_AREA_TRAPZ.value] = round(avg_avg_area,2)
    results_array[image_counter][Results.AVG_AREA_MIN.value] = round(avg_min,2)
    results_array[image_counter][Results.AVG_AREA_Q1.value] = round(avg_q1,2)
    results_array[image_counter][Results.AVG_AREA_Q2.value] = round(avg_q2,2)
    results_array[image_counter][Results.AVG_AREA_Q3.value] = round(avg_q3,2)
    results_array[image_counter][Results.AVG_AREA_MAX.value] = round(avg_max,2)
    results_array[image_counter][Results.AVG_AREA_IQR.value] = round(avg_iqr,2)
    results_array[image_counter][Results.AVG_AREA_STDDEV.value] = round(avg_std,2)

figure_area = plt.tight_layout()
figure_area = plt.show()

table_columns = []
for r in Results:
    table_columns.append(str(r.name))
df = pd.DataFrame(np.array(results_array), columns=table_columns)
print("- - - - - RESULTS ARRAY - - - - -")
display(df)

df.to_csv('Area/Result/Results.csv', index=False)
# END OF CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #