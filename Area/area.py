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
from scipy.integrate import simpson
from numpy import trapz
import imutils

# Read in the .jpgs and save into an image array, ensuring grayscale- - - - - - - - - - - - - - - - - - - - - - - - - - - #
image_array = []
image_names = []
for filename in glob.glob('Data\*.jpg'):
    im = Image.open(filename).convert('L') # convert image to grayscale
    res = im.point((lambda p: 256 if p>=200 else 0)) # convert each pixel into either black or white
    res.save(filename)

    arrayName = os.path.basename(filename)
    arrayName = arrayName.replace(".jpg","")
    image = cv2.imread(filename)
    image_array.append(image)
    image_names.append(arrayName)

# Loop through the image array to perform image processing- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
for image_counter,image in enumerate(image_array):
    coordinates = np.argwhere(image < 0.9)
    x_tuple, y_tuple, z_tuple = zip(*coordinates)

    y = np.array(y_tuple).tolist()
    x = np.array(x_tuple).tolist()
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
    
    for i in range(0, len(y)-1):
        for j in range(0, len(y)-i-1):
            if y[j] < y[j+1]:
                temp_x = x[j]
                x[j] = x[j+1]
                x[j+1] = temp_x

                temp_y = y[j]
                y[j] = y[j+1]
                y[j+1] = temp_y

    print(average_x)
    for i in range(0, len(x)):
        new_array_y.append(y[i])
        average_array_x.append(0)

        if x[i] < average_x: 
            c = 3
            new_array_x.append(average_x - x[i])
        else:
            new_array_x.append(x[i] - average_x)



    # print(new_array_x)
    # print(new_array_y)

    # plt.scatter(new_array_y, new_array_x)
    # plt.show()

    # plt.plot(new_array_y, new_array_x)
    # plt.plot(new_array_y, average_array_x)
    # plt.show()


    plt.rcParams["figure.figsize"] = [8, 1]
    plt.rcParams["figure.autolayout"] = True



    plt.fill_between(new_array_y, new_array_x, color="grey")
    plt.xlim(0, 600)
    plt.ylim(0, 20)
    # plt.fill_between(new_array_x, average_array_x, color="yellow")

    plt.show()

    total_area_trapz_x = trapz(new_array_x)
    print(image_names[image_counter] + " X area =" + str(total_area_trapz_x))

    total_area_trapz_y = trapz(new_array_y)
    print(image_names[image_counter] + " Y area =" + str(total_area_trapz_y))



# END OF CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #