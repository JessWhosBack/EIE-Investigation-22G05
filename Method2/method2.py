# EIE Investigation: "Which Hand?"
# Jesse van der Merwe (1829172) and Robyn Gebbie (2127777)
# ELEN4012A NOVEMBER 2022

# IMPORTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import cv2
import glob
import os	
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import trapz
from enum import Enum
import pandas as pd
from IPython.display import display
from scipy import signal
from scipy.fft import rfft, rfftfreq, irfft

class Results(Enum):
    FILENAME = 0
    PATIENT_NUMBER = 1
    DOMINANT_HAND = 2
    TREATED_HAND = 3
    TIME_PERIOD = 4
    PD_HAND = 5
    AREA_TRAPZ = 6
    MAX = 7
    STDDEV = 8
    AVG_AREA_TRAPZ = 9
    AVG_AREA_MAX = 10
    AVG_AREA_STDDEV = 11
    NUM_PEAKS = 12
    AVG_PEAK_DIST = 13
    
# Read in the .jpgs and save into an image array, ensuring grayscale- - - - - - - - - - - - - - - - - - - - - - - - - - - #
image_array = []
image_names = []
image_patient_number = []
image_time_frame = []
image_dominant_hand = []
image_treated_hand = []
image_PD_hand = []
file_count = 0

def get_time_period(image_name): 
    image_name = str.lower(image_name)

    if image_name.find("w") != -1: 
        period = image_name[0:image_name.find("w")]
        time =  [int(s) for s in period.split() if s.isdigit()]

        if period.find("one") != -1:
            output = "1W"
        else: 
            output = str(time[0]) + "W"
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
                return output
            except:
                pass # Presentation purposes, delete later
                # print("ERROR - m but no time")

    if image_name.find("y") != -1:
        period = image_name[0:image_name.find("y")]
        time =  [int(s) for s in period.split() if s.isdigit()]

        if period.find("one") != -1:
            output = "1Y"
            return output
        else: 
            try:
                output = str(time[0]) + "Y"
                return output
            except:
                print("ERROR - y but no time - " + str(image_name))

    if image_name.find("before") != -1: 
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
            return True
    else: 
        right_position = image_name.find("rt")
        if right_position == -1: 
            right_position = image_name.find("right")
            if right_position == -1: 
                return False
            else:
                return True
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
            return True
    else: 
        right_position = image_name.find("rt")
        if right_position == -1: 
            right_position = image_name.find("right")
            if right_position == -1: 
                return False
            else:
                return True
        else:
            return True

def is_PD_hand(patient_number):
    if patient_number == 3 or patient_number == 4 or patient_number == 7 or patient_number == 8 or patient_number == 16 or patient_number == 18 or patient_number == 28 or patient_number == 31 or patient_number == 33 or patient_number == 37 or patient_number == 38 or patient_number == 39 or patient_number == 40 or patient_number == 43 or patient_number == 44 or patient_number == 47 or patient_number == 48 or patient_number == 55 or patient_number == 56 or patient_number == 57 or patient_number == 59 or patient_number == 63 or patient_number == 68 or patient_number == 70 or patient_number == 71 or patient_number == 76 or patient_number == 77 or patient_number == 92 or patient_number == 100 or patient_number == 112 or patient_number == 113 or patient_number == 114 or patient_number == 120 or patient_number == 124:
        return True
    else:
        return False

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
            is_PD = is_PD_hand(patient_number)
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
                image_PD_hand.append(is_PD)
                file_count = file_count + 1

results_array = [[-1 for x in range(len(Results))] for y in range(file_count)] 

temp_counter_patient_5 = -1
# Loop through the image array to perform image processing- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
for image_counter, image in enumerate(image_array):
    temp_counter_patient_5 += 1
    temp_title = image_names[image_counter].replace("(5)_C__RECT", "")

    results_array[image_counter][Results.FILENAME.value] = image_names[image_counter]
    results_array[image_counter][Results.PATIENT_NUMBER.value] = image_patient_number[image_counter]
    results_array[image_counter][Results.TIME_PERIOD.value] = image_time_frame[image_counter]
    results_array[image_counter][Results.DOMINANT_HAND.value] = image_dominant_hand[image_counter]
    results_array[image_counter][Results.TREATED_HAND.value] = image_treated_hand[image_counter]
    results_array[image_counter][Results.PD_HAND.value] = image_PD_hand[image_counter]

    coordinates = np.argwhere(image < 0.9)
    # fig, (axs_original, axs_fft, axs_ifft, axs_area) = plt.subplots(4)

    try:
        # NOTE: The horizontal axis is denoted by y, and the vertical axis is denoted by x - No, this was not on purpose. Yes, it's an absolute pain.
        x_tuple, y_tuple, z_tuple = zip(*coordinates)

        x = np.array(x_tuple).tolist()
        y = np.array(y_tuple).tolist()
        z = np.array(z_tuple).tolist()
        
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

        # GRAPH 1: ORIGINAL 
        # axs_original.set_title("ORIGINAL GRAPH: " + str(temp_title))  
        # axs_original.plot(y, x)

        average_x = np.mean(x)  
        new_array_x = []
        new_array_y = []

        # Take the absolute value and shift the points down to be centered around the horizontal axis
        for i in range(0, len(x)):
            new_array_y.append(y[i])
            new_array_x.append(x[i]-average_x)
            
        data_step = 0.1
        n = len(new_array_y)
        yf = rfft(new_array_x)
        xf = rfftfreq(n, data_step)

        yf_abs = np.abs(yf)
        yf_max = np.max(yf_abs)

        # # GRAPH 2: FFT
        # axs_fft.set_title("FFT: " + str(temp_title))  
        # axs_fft.plot(xf, yf_abs)
        # axs_fft.set_xlim(0, 0.5)
        
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

        # # GRAPH 3: IFFT
        # axs_ifft.set_title("IFFT: " + str(temp_title))  
        # axs_ifft.plot(new_array_y, new_array_x)

        # if len(new_array_y) > len(new_f_clean):
        #     new_new_array_y = new_array_y
        #     new_new_array_y.pop(0)
        #     axs_ifft.plot(new_new_array_y, new_f_clean)
        # else:
        #     axs_ifft.plot(new_array_y, new_f_clean)

        # axs_ifft.set_xlim(0, 600)
        # axs_ifft.set_ylim(-20, 20)
        
        # Quantile values of the data
        min, q1, q2, q3, q90, max = np.quantile(new_array_x, [0, 0.25, 0.5, 0.75, 0.9, 1])
        iqr = q3-q1
        std = np.std(new_array_x)

        x_peaks = signal.find_peaks(np.array(new_f_clean))
        num_peaks = len(x_peaks[0])
        y_peaks_points = []
        x_peaks_points = []
        sum_peaks = 0

        for p in x_peaks[0]:
            x_peaks_points.append(new_f_clean[p])
            y_peaks_points.append(new_array_y[p])

        MIN_x_peaks = signal.find_peaks(np.array(-new_f_clean))
        MIN_num_peaks = len(MIN_x_peaks[0])
        MIN_y_peaks_points = []
        MIN_x_peaks_points = []

        for p in MIN_x_peaks[0]:
            MIN_x_peaks_points.append(new_f_clean[p])
            MIN_y_peaks_points.append(new_array_y[p])

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

        # METHOD: TRAPZ FORMULA (NUMPY)
        new_array_x_ABS = [abs(x) for x in new_f_clean]
        total_area_trapz_x = trapz(new_array_x_ABS) # Area under the curve, using numpy's trapz formula
        
        # # GRAPH 4: AREA GRAPH
        # axs_area.set_title("AREA UNDER CURVE: " + str(temp_title))  
        # axs_area.fill_between(new_array_y, new_array_x_ABS, color="grey")
        # axs_area.plot(new_array_y, new_array_x_ABS)
        # axs_area.set_xlim(0, 600)
        # axs_area.set_ylim(0, 20)

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
        print("ERROR: \t" + str(image_patient_number[image_counter]) + "\t -\t " + str(image_names[image_counter]))

    # plt.tight_layout()
    # plt.show()

# SAVING THE DATA:
table_columns = []
for r in Results:
    table_columns.append(str(r.name))
df = pd.DataFrame(np.array(results_array), columns=table_columns)
print("- - - - - RESULTS ARRAY - - - - -")
display(df)
df.to_csv('Method2/Results.csv', index=False)

# END OF CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #