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

class Results(Enum):
    FILENAME = 0
    AREA_TRAPZ = 1
    Q3 = 3
    IQR = 4

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

figure_area = plt.figure(figsize=(8,10))
figure_area = plt.title("Area")

results_array = [[-1 for x in range(file_count)] for y in range(len(Results))] 

# Loop through the image array to perform image processing- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
for image_counter, image in enumerate(image_array):
    results_array[Results.FILENAME.value][image_counter] = image_names[image_counter]

    # IMAGE PROCESSING TO GENERATE GRAPH OF HAND DRAWN LINE THAT HAS BEEN SHIFTED DOWN TO THE X-AXIS- - - - - - - - - - - #
    # NOTE: The horizontal axis is denoted by y, and the vertical axis is denoted by x (no, this was not on purpose)
    coordinates = np.argwhere(image < 0.9)
    x_tuple, y_tuple, z_tuple = zip(*coordinates)

    x = np.array(x_tuple).tolist()
    y = np.array(y_tuple).tolist()
    z = np.array(z_tuple).tolist()

    average_x = np.mean(x)
    max_x = np.max(x)
    min_x = np.min(x)
    x_adjustment = 10/100*max_x
   
    # Remove top and bottom of pixels of image to get rid of any remaining border
    tracker = 0
    for i in range(0, len(x)): 
        if x[tracker] > max_x - x_adjustment or x[tracker] < min_x + x_adjustment:
            y.pop(tracker)
            x.pop(tracker)
            tracker = tracker - 1
        tracker = tracker + 1

    new_array_x = []
    new_array_y = []
    average_array_x = []
    
    # Sort the array of pixels into an ordered array according to the horizontal x-axis
    for i in range(0, len(y)-1):
        for j in range(0, len(y)-i-1):
            if y[j] < y[j+1]:
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
    results_array[Results.AREA_TRAPZ.value][image_counter] = total_area_trapz_x
    figure_area = plt.text(400, 15, "Area: " + str(total_area_trapz_x), bbox=dict(facecolor='red', alpha=0.5))

    # Quantile values of the data
    min, q1, q2, q3, max = np.quantile(new_array_x, [0, 0.25, 0.5, 0.75, 1])
    iqr = q3-q1
    figure_area = plt.text(400, 10, "Q75: " + str(round(q3, 2)), bbox=dict(facecolor='red', alpha=0.5))
    results_array[Results.Q3.value][image_counter] = q3
    figure_area = plt.text(400, 5, "IQR: " + str(round(iqr, 2)), bbox=dict(facecolor='red', alpha=0.5))
    results_array[Results.IQR.value][image_counter] = iqr

    

figure_area = plt.tight_layout()
plt.show()

print(results_array)

# END OF CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #