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
from scipy import signal
from scipy.fft import rfft, rfftfreq, irfft
class Results(Enum):
    FILENAME = 0
    PATIENT_NUMBER = 1
    DOMINANT_HAND = 2
    TREATED_HAND = 3
    TIME_PERIOD = 4

    AREA_TRAPZ = 5
    MAX = 6
    STDDEV = 7

    AVG_AREA_TRAPZ = 8
    AVG_AREA_MAX = 9
    AVG_AREA_STDDEV = 10

    NUM_PEAKS = 11
    AVG_PEAK_DIST = 12
    
# Read in the .jpgs and save into an image array, ensuring grayscale- - - - - - - - - - - - - - - - - - - - - - - - - - - #
image_array = []
image_names = []
image_patient_number = []
image_time_frame = []
image_dominant_hand = []
image_treated_hand = []
file_count = 0

def get_time_period(image_name): 
    image_name = str.lower(image_name)
    print(image_name)

    if image_name.find("w") != -1: 
        period = image_name[0:image_name.find("w")]
        time =  [int(s) for s in period.split() if s.isdigit()]

        if period.find("one") != -1:
            output = "1W"
        else: 
            output = str(time[0]) + "W"
        print(output)
        return output

    if image_name.find("m") != -1:
        period = image_name[0:image_name.find("m")]
        time =  [int(s) for s in period.split() if s.isdigit()]

        if period.find("one") != -1:
            output = "1M"
            return output

        else:
            try:
                output = str(time[0]) + "M"
                print(output)
                return output
            except:
                print("ERROR")


    if image_name.find("y") != -1:
        period = image_name[0:image_name.find("y")]
        time =  [int(s) for s in period.split() if s.isdigit()]

        if period.find("one") != -1:
            output = "1Y"
            print(output)
            return output
        else: 
            try:
                output = str(time[0]) + "Y"
                print(output)
                return output
            except:
                print("ERROR")

    if image_name.find("before") != -1: 
        print("before")
        return "before"

    return -1

def is_treated_hand(image_name, patient_number): 
    image_name = str.lower(image_name)

    if patient_number == 6 or patient_number == 17 or patient_number == 22 or patient_number == 32 or patient_number == 74 or patient_number == 85 or patient_number == 87 or patient_number == 109 or patient_number == 111 or patient_number == 115 or patient_number == 116  or patient_number == 8 or patient_number == 16 or patient_number == 31 or patient_number == 39 or patient_number == 40 or patient_number == 47 or patient_number == 56 or patient_number == 57 or patient_number == 124:
        left_position = image_name.find("lt")
        if left_position == -1:
            left_position = image_name.find("left")
            if left_position == -1:
                return False
        else:
            return True
    else: 
        right_position = image_name.find("rt")
        if right_position == -1: 
            right_position = image_name.find("right")
            if right_position == -1: 
                return False
        else:
            return True

def is_dominant_hand(image_name, patient_number):
    image_name = str.lower(image_name)

    if patient_number == 17 or patient_number == 22 or patient_number == 32 or patient_number == 56 or patient_number == 74 or patient_number == 87 or patient_number == 102 or patient_number == 109 or patient_number == 111 or patient_number == 115 or patient_number == 116 or patient_number == 117:
        left_position = image_name.find("lt")
        if left_position == -1:
            left_position = image_name.find("left")
            if left_position == -1:
                return False
        else:
            return True
    else: 
        right_position = image_name.find("rt")
        if right_position == -1: 
            right_position = image_name.find("right")
            if right_position == -1: 
                return False
        else:
            return True

for outer_foldername in glob.glob('Data\Cropped\*'):
    for foldername in glob.glob(outer_foldername + '\*'):
        patient_number = os.path.basename(foldername)
        patient_number = patient_number.replace("#", "")

        for filename in glob.glob(foldername + "\DrawingC\Rectangles\*.jpg"):
            arrayName = os.path.basename(filename)
            arrayName = arrayName.replace(".jpg","")

            time_period = get_time_period(arrayName)
            is_dominant = is_dominant_hand(arrayName, patient_number)
            is_treated = is_treated_hand(arrayName, patient_number)
            if time_period != -1:
                im = Image.open(filename).convert('L') # convert image to grayscale
                res = im.point((lambda p: 256 if p>=200 else 0)) # convert each pixel into either black or white
                res.save(filename)

                image = cv2.imread(filename)
                image_array.append(image)
                image_names.append(arrayName)
                image_patient_number.append(patient_number)
                image_time_frame.append(time_period)
                image_dominant_hand.append(is_dominant)
                image_treated_hand.append(is_treated)
                file_count = file_count + 1

results_array = [[-1 for x in range(len(Results))] for y in range(file_count)] 

# Loop through the image array to perform image processing- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
for image_counter, image in enumerate(image_array):
    results_array[image_counter][Results.FILENAME.value] = image_names[image_counter]
    results_array[image_counter][Results.PATIENT_NUMBER.value] = image_patient_number[image_counter]
    results_array[image_counter][Results.TIME_PERIOD.value] = image_time_frame[image_counter]
    results_array[image_counter][Results.DOMINANT_HAND.value] = image_dominant_hand[image_counter]
    results_array[image_counter][Results.TREATED_HAND.value] = image_treated_hand[image_counter]

    coordinates = np.argwhere(image < 0.9)
    try:
        # NOTE: The horizontal axis is denoted by y, and the vertical axis is denoted by x - No, this was not on purpose. Yes, it's an absolute pain.
        x_tuple, y_tuple, z_tuple = zip(*coordinates)

        x = np.array(x_tuple).tolist()
        y = np.array(y_tuple).tolist()
        z = np.array(z_tuple).tolist()

        average_x = np.mean(x)  
        new_array_x = []
        new_array_x_ABS = []
        new_array_y = []
        
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

        # Take the absolute value and shift the points down to be centered around the horizontal axis
        for i in range(0, len(x)):
            new_array_y.append(y[i])
            new_array_x.append(x[i]-average_x)
            
            # Use the below code to shift the points down to be centered around the horizontal axis AND be the absolute version of the graph
            if x[i] < average_x: 
                c = 3
                new_array_x_ABS.append(average_x - x[i])
            else:
                new_array_x_ABS.append(x[i] - average_x)

        # # Plot the shifted points as a line graph 
        # figure_fft = plt.subplot(math.ceil(file_count/2), 2, image_counter+1)
        # figure_fft = plt.title(str(image_names[image_counter]))  

        # # figure_fft = plt.fill_between(new_array_y, new_array_x, color="grey")
        # figure_fft = plt.plot(new_array_y, new_array_x)

        sos = signal.iirfilter(4, Wn=[0.1, 2.5], fs=30, btype="bandpass", ftype="butter", output="sos")
        yfilt = signal.sosfilt(sos, new_array_x)

        data_step = 0.1
        n = len(new_array_y)
        yf = rfft(new_array_x)
        xf = rfftfreq(n, data_step)

        # figure_fft = plt.plot(xf, np.abs(yf))

        yf_abs = np.abs(yf)
        yf_max = np.max(yf_abs)
        print(yf_max)
        
        multiplier = 5
        MIN_multiplier = 5
        indices = yf_abs > (multiplier/100*yf_max)
        yf_clean = indices*yf
        new_f_clean = irfft(yf_clean)
        x_peaks = signal.find_peaks(np.array(new_f_clean))
        MIN_x_peaks = signal.find_peaks(np.array(-new_f_clean))

        while len(x_peaks[0]) > 50 or len(MIN_x_peaks[0]) > 50:
            indices = yf_abs > (multiplier/100*yf_max)
            yf_clean = indices*yf
            new_f_clean = irfft(yf_clean)
            x_peaks = signal.find_peaks(np.array(new_f_clean))
            MIN_x_peaks = signal.find_peaks(np.array(-new_f_clean))

            multiplier = multiplier+5

        if len(new_array_y) > len(new_f_clean):
            new_new_array_y = new_array_y
            new_new_array_y.pop(0)
        #     figure_fft = plt.plot(new_new_array_y, new_f_clean)
        # else:
        #     figure_fft = plt.plot(new_array_y, new_f_clean)

        # EXTRACTING OF NUMERICAL DATA FROM THE ABOVE GRAPH - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
        total_area_trapz_x = trapz(new_array_x_ABS) # Area under the curve, using numpy's trapz formula
        # figure_fft = plt.text(100, 10, "Abs Area: " + str(round(total_area_trapz_x, 2)), bbox=dict(facecolor='beige', alpha=0.5))
        # figure_fft = plt.xlim(0, 600)
        # figure_fft = plt.ylim(-20, 20)
        
        # Quantile values of the data
        min, q1, q2, q3, q90, max = np.quantile(new_array_x, [0, 0.25, 0.5, 0.75, 0.9, 1])
        iqr = q3-q1
        std = np.std(new_array_x)

        x_peaks = signal.find_peaks(np.array(new_f_clean))
        num_peaks = len(x_peaks[0])
        # figure_fft = plt.text(300, 10, "NUM PEAKS: " + str(num_peaks), bbox=dict(facecolor='beige', alpha=0.5))

        y_peaks_points = []
        x_peaks_points = []
        sum_peaks = 0
        for p in x_peaks[0]:
            x_peaks_points.append(new_f_clean[p])
            y_peaks_points.append(new_array_y[p])
        # figure_fft = plt.plot(y_peaks_points, x_peaks_points, marker="x", linestyle="None", color='purple')

        MIN_x_peaks = signal.find_peaks(np.array(-new_f_clean))
        MIN_num_peaks = len(MIN_x_peaks[0])
        # figure_fft = plt.text(500, 10, "NUM MIN PEAKS: " + str(MIN_num_peaks), bbox=dict(facecolor='beige', alpha=0.5))

        MIN_y_peaks_points = []
        MIN_x_peaks_points = []
        for p in MIN_x_peaks[0]:
            MIN_x_peaks_points.append(new_f_clean[p])
            MIN_y_peaks_points.append(new_array_y[p])
        # figure_fft = plt.plot(MIN_y_peaks_points, MIN_x_peaks_points, marker="x", linestyle="None", color='green')

        peakmin_distance_array = []
        for i in range(len(x_peaks_points)):
            if y_peaks_points[i] < MIN_y_peaks_points[i]:
                if i == 0:
                    peakmin_distance_array.append(abs(x_peaks_points[i] - MIN_x_peaks_points[i]))
                else:
                    peakmin_distance_array.append(abs(x_peaks_points[i] - MIN_x_peaks_points[i-1]))
                    peakmin_distance_array.append(abs(x_peaks_points[i] - MIN_x_peaks_points[i]))
            else:
                peakmin_distance_array.append(abs(x_peaks_points[i] - MIN_x_peaks_points[i]))
                if i < len(x_peaks_points)-1:
                    peakmin_distance_array.append(abs(x_peaks_points[i] - MIN_x_peaks_points[i+1]))

        average_peakmin_distance = np.mean(peakmin_distance_array)
        # figure_fft = plt.text(100, -10, "Avg Peak Distance: " + str(round(average_peakmin_distance, 2)), bbox=dict(facecolor='beige', alpha=0.5))
        # figure_fft = plt.text(300, -10, "NEW 1: " + str(round(average_peakmin_distance/num_peaks, 2)), bbox=dict(facecolor='beige', alpha=0.5))
        # figure_fft = plt.text(500, -10, "NEW 2: " + str(round(average_peakmin_distance*num_peaks, 2)), bbox=dict(facecolor='beige', alpha=0.5))

        results_array[image_counter][Results.AREA_TRAPZ.value] = total_area_trapz_x
        results_array[image_counter][Results.MAX.value] = max
        results_array[image_counter][Results.STDDEV.value] = std

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
                        
            temp_area_x = trapz(temp_array_x, temp_array_y)
            average_areas.append(temp_area_x)   
            temp_counter = temp_counter + 1

        # Quantile values of the data
        avg_avg_area = np.mean(average_areas)
        avg_min, avg_q1, avg_q2, avg_q3, avg_max = np.quantile(average_areas, [0, 0.25, 0.5, 0.75, 1])
        avg_iqr = avg_q3-avg_q1
        avg_std = np.std(average_areas)

        results_array[image_counter][Results.AVG_AREA_TRAPZ.value] = avg_avg_area
        results_array[image_counter][Results.AVG_AREA_MAX.value] = avg_max
        results_array[image_counter][Results.AVG_AREA_STDDEV.value] = avg_std

        results_array[image_counter][Results.NUM_PEAKS.value] = num_peaks
        results_array[image_counter][Results.AVG_PEAK_DIST.value] = average_peakmin_distance

    except:
        print("ERROR: " + str(image_patient_number[image_counter]) + " - " + str(image_names[image_counter]))

# figure_fft = plt.tight_layout()
# figure_fft = plt.show()

table_columns = []
for r in Results:
    table_columns.append(str(r.name))
df = pd.DataFrame(np.array(results_array), columns=table_columns)
print("- - - - - RESULTS ARRAY - - - - -")
display(df)

df.to_csv('Area/Result/Results.csv', index=False)
# END OF CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #