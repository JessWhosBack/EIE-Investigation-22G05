# EIE Investigation: "Which Hand?"
# Jesse van der Merwe (1829172) and Robyn Gebbie (2127777)
# ELEN4012A NOVEMBER 2022

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# COPYRIGHT NOTICE: 
# This code is taken from Kelvin da Silva's Master's project which involved the classification of tremors. 
# This can be found at: https://github.com/kdasilva835842/tremor_classification
# 
# Kelvin's code is based on the OpenCV Text Detection (EAST text detector) article by Adrian Rosebrock (20/08/2021).
# This can be found at: https://pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/
# 
# The code has been further modified, with permission from Kelvin, to suit the needs of this project. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# IT SHOULD BE NOTED THAT "DOMINANT" AND "NON-DOMINANT" HAND REFERS TO "TREATED" AND "NON-TREATED" HANDS. 
# YES THIS IS CONFUSING 
# YES IT WAS TOO LATE TO CHANGE IT 

# class Results(Enum):
    # FILENAME = 0
    # PATIENT_NUMBER = 1
    # DOMINANT_HAND = 2
    # TREATED_HAND = 3
    # TIME_PERIOD = 4

    # AREA_TRAPZ = 5
    # MAX = 6
    # STDDEV = 7

    # AVG_AREA_TRAPZ = 8
    # AVG_AREA_MAX = 9
    # AVG_AREA_STDDEV = 10

    # NUM_PEAKS = 11
    # AVG_PEAK_DIST = 12

patient_number_array = []
patient_dominant_hand = []
patient_treated_hand = []
patient_time_array = []

patient_area_trapz = []
patient_avg_area_trapz = []
patient_avg_std_dev_array = []

patient_num_peaks = []
patient_avg_peak_dist = []
patient_determinator_1 = []
patient_determinator_2 = []

with open('Area\Results.csv', 'r') as theFile: 
    reader = csv.DictReader(theFile)
    for line in reader: 
        patient_number_array.append(line['PATIENT_NUMBER'])
        patient_dominant_hand.append(line['DOMINANT_HAND'])
        patient_treated_hand.append(line['TREATED_HAND'])
        patient_time_array.append(line['TIME_PERIOD'])

        patient_area_trapz.append(line['AREA_TRAPZ'])
        patient_avg_area_trapz.append(line['AVG_AREA_TRAPZ'])
        patient_avg_std_dev_array.append(line['AVG_AREA_STDDEV'])

        num_peaks = line['NUM_PEAKS']
        avg_peak_dist = line['AVG_PEAK_DIST']

        patient_num_peaks.append(num_peaks)
        patient_avg_peak_dist.append(avg_peak_dist)
        patient_determinator_1.append(float(avg_peak_dist)/float(num_peaks))
        patient_determinator_2.append(float(avg_peak_dist)*float(num_peaks))

   
n = len(patient_number_array)

for i in range(0, n):
    for j in range(0, n-i-1):
        if patient_number_array[j] > patient_number_array[j+1]:
            temp = patient_number_array[j]
            patient_number_array[j] = patient_number_array[j+1]
            patient_number_array[j+1] = temp

            temp = patient_dominant_hand[j]
            patient_dominant_hand[j] = patient_dominant_hand[j+1]
            patient_dominant_hand[j+1] = temp

            temp = patient_treated_hand[j]
            patient_treated_hand[j] = patient_treated_hand[j+1]
            patient_treated_hand[j+1] = temp

            temp = patient_time_array[j]
            patient_time_array[j] = patient_time_array[j+1]
            patient_time_array[j+1] = temp

            temp = patient_area_trapz[j]
            patient_area_trapz[j] = patient_area_trapz[j+1]
            patient_area_trapz[j+1] = temp

            temp = patient_avg_area_trapz[j]
            patient_avg_area_trapz[j] = patient_avg_area_trapz[j+1]
            patient_avg_area_trapz[j+1] = temp
            
            temp = patient_avg_std_dev_array[j]
            patient_avg_std_dev_array[j] = patient_avg_std_dev_array[j+1]
            patient_avg_std_dev_array[j+1] = temp

            temp = patient_num_peaks[j]
            patient_num_peaks[j] = patient_num_peaks[j+1]
            patient_num_peaks[j+1] = temp

            temp = patient_avg_peak_dist[j]
            patient_avg_peak_dist[j] = patient_avg_peak_dist[j+1]
            patient_avg_peak_dist[j+1] = temp

            temp = patient_determinator_1[j]
            patient_determinator_1[j] = patient_determinator_1[j+1]
            patient_determinator_1[j+1] = temp
            
            temp = patient_determinator_2[j]
            patient_determinator_2[j] = patient_determinator_2[j+1]
            patient_determinator_2[j+1] = temp

# new1_patient_time_array = patient_time_array.copy()
# new1_patient_determinator_1 = patient_determinator_1.copy()
# new1_patient_num_peaks = patient_num_peaks.copy()
# new1_patient_avg_peak_dist = patient_avg_peak_dist.copy()
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         if new1_patient_determinator_1[j] > new1_patient_determinator_1[j+1]:
#             temp = new1_patient_determinator_1[j]
#             new1_patient_determinator_1[j] = new1_patient_determinator_1[j+1]
#             new1_patient_determinator_1[j+1] = temp

#             temp = new1_patient_time_array[j]
#             new1_patient_time_array[j] = new1_patient_time_array[j+1]
#             new1_patient_time_array[j+1] = temp

#             temp = new1_patient_num_peaks[j]
#             new1_patient_num_peaks[j] = new1_patient_num_peaks[j+1]
#             new1_patient_num_peaks[j+1] = temp

#             temp = new1_patient_avg_peak_dist[j]
#             new1_patient_avg_peak_dist[j] = new1_patient_avg_peak_dist[j+1]
#             new1_patient_avg_peak_dist[j+1] = temp

# new2_patient_time_array = patient_time_array.copy()
# new2_patient_determinator_2 = patient_determinator_2.copy()
# new2_patient_num_peaks = patient_num_peaks.copy()
# new2_patient_avg_peak_dist = patient_avg_peak_dist.copy()

# for i in range(0, n):
#     for j in range(0, n-i-1):
#         if new2_patient_determinator_2[j] > new2_patient_determinator_2[j+1]:

#             temp = new2_patient_determinator_2[j]
#             new2_patient_determinator_2[j] = new2_patient_determinator_2[j+1]
#             new2_patient_determinator_2[j+1] = temp

#             temp = new2_patient_time_array[j]
#             new2_patient_time_array[j] = new2_patient_time_array[j+1]
#             new2_patient_time_array[j+1] = temp

#             temp = new2_patient_num_peaks[j]
#             new2_patient_num_peaks[j] = new2_patient_num_peaks[j+1]
#             new2_patient_num_peaks[j+1] = temp

#             temp = new2_patient_avg_peak_dist[j]
#             new2_patient_avg_peak_dist[j] = new2_patient_avg_peak_dist[j+1]
#             new2_patient_avg_peak_dist[j+1] = temp

### THE BELOW CODE WORKS BUT ALSO LIKE WTF IT'S SO LONG
D_patient_number_array_avg_std_dev = []
D_patient_number_array_avg_std_dev.append(1)
D_patient_counter_avg_std_dev = 0

D_time_before_avg_std_dev = []
D_time_1W_avg_std_dev = []
D_time_1M_avg_std_dev = []
D_time_3M_avg_std_dev = []
D_time_6M_avg_std_dev = []
D_time_1Y_avg_std_dev = []
D_time_2Y_avg_std_dev = []
D_time_3Y_avg_std_dev = []
D_time_4Y_avg_std_dev = []

D_time_before_avg_std_dev.append(0)
D_time_1W_avg_std_dev.append(0)
D_time_1M_avg_std_dev.append(0)
D_time_3M_avg_std_dev.append(0)
D_time_6M_avg_std_dev.append(0)
D_time_1Y_avg_std_dev.append(0)
D_time_2Y_avg_std_dev.append(0)
D_time_3Y_avg_std_dev.append(0)
D_time_4Y_avg_std_dev.append(0)

ND_patient_number_array_avg_std_dev = []
ND_patient_number_array_avg_std_dev.append(1)
ND_patient_counter_avg_std_dev = 0

ND_time_before_avg_std_dev = []
ND_time_1W_avg_std_dev = []
ND_time_1M_avg_std_dev = []
ND_time_3M_avg_std_dev = []
ND_time_6M_avg_std_dev = []
ND_time_1Y_avg_std_dev = []
ND_time_2Y_avg_std_dev = []
ND_time_3Y_avg_std_dev = []
ND_time_4Y_avg_std_dev = []

ND_time_before_avg_std_dev.append(0)
ND_time_1W_avg_std_dev.append(0)
ND_time_1M_avg_std_dev.append(0)
ND_time_3M_avg_std_dev.append(0)
ND_time_6M_avg_std_dev.append(0)
ND_time_1Y_avg_std_dev.append(0)
ND_time_2Y_avg_std_dev.append(0)
ND_time_3Y_avg_std_dev.append(0)
ND_time_4Y_avg_std_dev.append(0)

max_std_dev = 0.0
min_std_dev = 100.0

for i in range(0, n):    
    if float(patient_avg_std_dev_array[i]) > float(max_std_dev):
        max_std_dev = patient_avg_std_dev_array[i]

    if float(patient_avg_std_dev_array[i]) < float(min_std_dev) and float(patient_avg_std_dev_array[i]) >= float(0.0):
        min_std_dev = patient_avg_std_dev_array[i]

    if patient_treated_hand[i] == 'True':
        if int(patient_number_array[i]) != int(D_patient_number_array_avg_std_dev[D_patient_counter_avg_std_dev]):
            D_patient_number_array_avg_std_dev.append(patient_number_array[i])
            D_patient_counter_avg_std_dev = D_patient_counter_avg_std_dev + 1 
            D_time_before_avg_std_dev.append(0)
            D_time_1W_avg_std_dev.append(0)
            D_time_1M_avg_std_dev.append(0)
            D_time_3M_avg_std_dev.append(0)
            D_time_6M_avg_std_dev.append(0)
            D_time_1Y_avg_std_dev.append(0)
            D_time_2Y_avg_std_dev.append(0)
            D_time_3Y_avg_std_dev.append(0)
            D_time_4Y_avg_std_dev.append(0)
            
        if patient_time_array[i] == "before":
            D_time_before_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1W":
            D_time_1W_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1M":
            D_time_1M_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "3M":
            D_time_3M_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "6M":
            D_time_6M_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1Y":
            D_time_1Y_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "2Y":
            D_time_2Y_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "3Y":
            D_time_3Y_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "4Y":
            D_time_4Y_avg_std_dev[D_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
            
    else:
        if int(patient_number_array[i]) != int(ND_patient_number_array_avg_std_dev[ND_patient_counter_avg_std_dev]):
            ND_patient_number_array_avg_std_dev.append(patient_number_array[i])
            ND_patient_counter_avg_std_dev = ND_patient_counter_avg_std_dev + 1 
            ND_time_before_avg_std_dev.append(0)
            ND_time_1W_avg_std_dev.append(0)
            ND_time_1M_avg_std_dev.append(0)
            ND_time_3M_avg_std_dev.append(0)
            ND_time_6M_avg_std_dev.append(0)
            ND_time_1Y_avg_std_dev.append(0)
            ND_time_2Y_avg_std_dev.append(0)
            ND_time_3Y_avg_std_dev.append(0)
            ND_time_4Y_avg_std_dev.append(0)

        if patient_time_array[i] == "before":
            ND_time_before_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1W":
            ND_time_1W_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1M":
            ND_time_1M_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "3M":
            ND_time_3M_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "6M":
            ND_time_6M_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1Y":
            ND_time_1Y_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "2Y":
            ND_time_2Y_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "3Y":
            ND_time_3Y_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "4Y":
            ND_time_4Y_avg_std_dev[ND_patient_counter_avg_std_dev] = patient_avg_std_dev_array[i]
                
D_data_avg_std_dev = {'Patient': D_patient_number_array_avg_std_dev, 'Before' : D_time_before_avg_std_dev, '1 Week' : D_time_1W_avg_std_dev, '1 Month' : D_time_1M_avg_std_dev, '3 Months': D_time_3M_avg_std_dev, '6 Months': D_time_6M_avg_std_dev, '1 Year': D_time_1Y_avg_std_dev, '2 Years': D_time_2Y_avg_std_dev, '3 Years':D_time_3Y_avg_std_dev, '4 Years':D_time_4Y_avg_std_dev }
D_df_avg_std_dev = pd.DataFrame(D_data_avg_std_dev)
D_df_avg_std_dev.to_csv('RESULTS/D_AvgStdDev.csv', index=False)

ND_data_avg_std_dev = {'Patient': ND_patient_number_array_avg_std_dev, 'Before' : ND_time_before_avg_std_dev, '1 Week' : ND_time_1W_avg_std_dev, '1 Month' : ND_time_1M_avg_std_dev, '3 Months': ND_time_3M_avg_std_dev, '6 Months': ND_time_6M_avg_std_dev, '1 Year': ND_time_1Y_avg_std_dev, '2 Years': ND_time_2Y_avg_std_dev, '3 Years':ND_time_3Y_avg_std_dev, '4 Years':ND_time_4Y_avg_std_dev }
ND_df_avg_std_dev = pd.DataFrame(ND_data_avg_std_dev)
ND_df_avg_std_dev.to_csv('RESULTS/ND_AvgStdDev.csv', index=False)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

D_patient_number_array_avg_area_trapz = []
D_patient_number_array_avg_area_trapz.append(1)
D_patient_counter_avg_area_trapz = 0

D_time_before_avg_area_trapz = []
D_time_1W_avg_area_trapz = []
D_time_1M_avg_area_trapz = []
D_time_3M_avg_area_trapz = []
D_time_6M_avg_area_trapz = []
D_time_1Y_avg_area_trapz = []
D_time_2Y_avg_area_trapz = []
D_time_3Y_avg_area_trapz = []
D_time_4Y_avg_area_trapz = []

D_time_before_avg_area_trapz.append(0)
D_time_1W_avg_area_trapz.append(0)
D_time_1M_avg_area_trapz.append(0)
D_time_3M_avg_area_trapz.append(0)
D_time_6M_avg_area_trapz.append(0)
D_time_1Y_avg_area_trapz.append(0)
D_time_2Y_avg_area_trapz.append(0)
D_time_3Y_avg_area_trapz.append(0)
D_time_4Y_avg_area_trapz.append(0)

ND_patient_number_array_avg_area_trapz = []
ND_patient_number_array_avg_area_trapz.append(1)
ND_patient_counter_avg_area_trapz = 0

ND_time_before_avg_area_trapz = []
ND_time_1W_avg_area_trapz = []
ND_time_1M_avg_area_trapz = []
ND_time_3M_avg_area_trapz = []
ND_time_6M_avg_area_trapz = []
ND_time_1Y_avg_area_trapz = []
ND_time_2Y_avg_area_trapz = []
ND_time_3Y_avg_area_trapz = []
ND_time_4Y_avg_area_trapz = []

ND_time_before_avg_area_trapz.append(0)
ND_time_1W_avg_area_trapz.append(0)
ND_time_1M_avg_area_trapz.append(0)
ND_time_3M_avg_area_trapz.append(0)
ND_time_6M_avg_area_trapz.append(0)
ND_time_1Y_avg_area_trapz.append(0)
ND_time_2Y_avg_area_trapz.append(0)
ND_time_3Y_avg_area_trapz.append(0)
ND_time_4Y_avg_area_trapz.append(0)

max_area = 0.0
min_area = 100.0

for i in range(0, n):    
    if float(patient_avg_area_trapz[i]) > float(max_area):
        max_area = patient_avg_area_trapz[i]

    if float(patient_avg_area_trapz[i]) < float(min_area) and float(patient_avg_area_trapz[i]) >= float(0.0):
        min_area = patient_avg_area_trapz[i]

    if patient_treated_hand[i] == 'True':
        if int(patient_number_array[i]) != int(D_patient_number_array_avg_area_trapz[D_patient_counter_avg_area_trapz]):
            D_patient_number_array_avg_area_trapz.append(patient_number_array[i])
            D_patient_counter_avg_area_trapz = D_patient_counter_avg_area_trapz + 1 
            D_time_before_avg_area_trapz.append(0)
            D_time_1W_avg_area_trapz.append(0)
            D_time_1M_avg_area_trapz.append(0)
            D_time_3M_avg_area_trapz.append(0)
            D_time_6M_avg_area_trapz.append(0)
            D_time_1Y_avg_area_trapz.append(0)
            D_time_2Y_avg_area_trapz.append(0)
            D_time_3Y_avg_area_trapz.append(0)
            D_time_4Y_avg_area_trapz.append(0)
            
        if patient_time_array[i] == "before":
            D_time_before_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1W":
            D_time_1W_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1M":
            D_time_1M_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "3M":
            D_time_3M_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "6M":
            D_time_6M_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1Y":
            D_time_1Y_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "2Y":
            D_time_2Y_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "3Y":
            D_time_3Y_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "4Y":
            D_time_4Y_avg_area_trapz[D_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
            
    else:
        if int(patient_number_array[i]) != int(ND_patient_number_array_avg_area_trapz[ND_patient_counter_avg_area_trapz]):
            ND_patient_number_array_avg_area_trapz.append(patient_number_array[i])
            ND_patient_counter_avg_area_trapz = ND_patient_counter_avg_area_trapz + 1 
            ND_time_before_avg_area_trapz.append(0)
            ND_time_1W_avg_area_trapz.append(0)
            ND_time_1M_avg_area_trapz.append(0)
            ND_time_3M_avg_area_trapz.append(0)
            ND_time_6M_avg_area_trapz.append(0)
            ND_time_1Y_avg_area_trapz.append(0)
            ND_time_2Y_avg_area_trapz.append(0)
            ND_time_3Y_avg_area_trapz.append(0)
            ND_time_4Y_avg_area_trapz.append(0)

        if patient_time_array[i] == "before":
            ND_time_before_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1W":
            ND_time_1W_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1M":
            ND_time_1M_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "3M":
            ND_time_3M_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "6M":
            ND_time_6M_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1Y":
            ND_time_1Y_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "2Y":
            ND_time_2Y_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "3Y":
            ND_time_3Y_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "4Y":
            ND_time_4Y_avg_area_trapz[ND_patient_counter_avg_area_trapz] = patient_avg_area_trapz[i]
                
D_data_avg_area_trapz = {'Patient': D_patient_number_array_avg_area_trapz, 'Before' : D_time_before_avg_area_trapz, '1 Week' : D_time_1W_avg_area_trapz, '1 Month' : D_time_1M_avg_area_trapz, '3 Months': D_time_3M_avg_area_trapz, '6 Months': D_time_6M_avg_area_trapz, '1 Year': D_time_1Y_avg_area_trapz, '2 Years': D_time_2Y_avg_area_trapz, '3 Years':D_time_3Y_avg_area_trapz, '4 Years':D_time_4Y_avg_area_trapz }
D_df_avg_area_trapz = pd.DataFrame(D_data_avg_area_trapz)
D_df_avg_area_trapz.to_csv('RESULTS/D_AreaTrapz.csv', index=False)

ND_data_avg_area_trapz = {'Patient': ND_patient_number_array_avg_area_trapz, 'Before' : ND_time_before_avg_area_trapz, '1 Week' : ND_time_1W_avg_area_trapz, '1 Month' : ND_time_1M_avg_area_trapz, '3 Months': ND_time_3M_avg_area_trapz, '6 Months': ND_time_6M_avg_area_trapz, '1 Year': ND_time_1Y_avg_area_trapz, '2 Years': ND_time_2Y_avg_area_trapz, '3 Years':ND_time_3Y_avg_area_trapz, '4 Years':ND_time_4Y_avg_area_trapz }
ND_df_avg_area_trapz = pd.DataFrame(ND_data_avg_area_trapz)
ND_df_avg_area_trapz.to_csv('RESULTS/ND_AreaTrapz.csv', index=False)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# WE ARE LOOKING HERE NOW! 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

D_patient_number_array_det_2 = []
D_patient_number_array_det_2.append(1)
D_patient_counter_det_2 = 0

D_time_before_det_2 = []
D_time_1W_det_2 = []
D_time_1M_det_2 = []
D_time_3M_det_2 = []
D_time_6M_det_2 = []
D_time_1Y_det_2 = []
D_time_2Y_det_2 = []
D_time_3Y_det_2 = []
D_time_4Y_det_2 = []

D_time_before_det_2.append(0)
D_time_1W_det_2.append(0)
D_time_1M_det_2.append(0)
D_time_3M_det_2.append(0)
D_time_6M_det_2.append(0)
D_time_1Y_det_2.append(0)
D_time_2Y_det_2.append(0)
D_time_3Y_det_2.append(0)
D_time_4Y_det_2.append(0)

ND_patient_number_array_det_2 = []
ND_patient_number_array_det_2.append(1)
ND_patient_counter_det_2 = 0

ND_time_before_det_2 = []
ND_time_1W_det_2 = []
ND_time_1M_det_2 = []
ND_time_3M_det_2 = []
ND_time_6M_det_2 = []
ND_time_1Y_det_2 = []
ND_time_2Y_det_2 = []
ND_time_3Y_det_2 = []
ND_time_4Y_det_2 = []

ND_time_before_det_2.append(0)
ND_time_1W_det_2.append(0)
ND_time_1M_det_2.append(0)
ND_time_3M_det_2.append(0)
ND_time_6M_det_2.append(0)
ND_time_1Y_det_2.append(0)
ND_time_2Y_det_2.append(0)
ND_time_3Y_det_2.append(0)
ND_time_4Y_det_2.append(0)

D_patient_hand_array_det_2 = []
ND_patient_hand_array_det_2 = []

max_det_2 = 0.0
min_det_2 = 100.0

for i in range(0, n):  
    if float(patient_determinator_2[i]) > float(max_det_2):
        max_det_2 = patient_determinator_2[i]

    if float(patient_determinator_2[i]) < float(min_det_2) and float(patient_determinator_2[i]) >= float(0.0):
        min_det_2 = patient_determinator_2[i]

    if patient_treated_hand[i] == 'True':
        if int(patient_number_array[i]) != int(D_patient_number_array_det_2[D_patient_counter_det_2]):
            D_patient_hand_array_det_2.append(patient_dominant_hand[i])
            D_patient_number_array_det_2.append(patient_number_array[i])
            D_patient_counter_det_2 = D_patient_counter_det_2 + 1 
            D_time_before_det_2.append(0)
            D_time_1W_det_2.append(0)
            D_time_1M_det_2.append(0)
            D_time_3M_det_2.append(0)
            D_time_6M_det_2.append(0)
            D_time_1Y_det_2.append(0)
            D_time_2Y_det_2.append(0)
            D_time_3Y_det_2.append(0)
            D_time_4Y_det_2.append(0)
            
        if patient_time_array[i] == "before":
            D_time_before_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "1W":
            D_time_1W_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "1M":
            D_time_1M_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "3M":
            D_time_3M_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "6M":
            D_time_6M_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "1Y":
            D_time_1Y_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "2Y":
            D_time_2Y_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "3Y":
            D_time_3Y_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "4Y":
            D_time_4Y_det_2[D_patient_counter_det_2] = patient_determinator_2[i]
            
    else:
        if int(patient_number_array[i]) != int(ND_patient_number_array_det_2[ND_patient_counter_det_2]):
            ND_patient_hand_array_det_2.append(patient_dominant_hand[i])
            ND_patient_number_array_det_2.append(patient_number_array[i])
            ND_patient_counter_det_2 = ND_patient_counter_det_2 + 1 
            ND_time_before_det_2.append(0)
            ND_time_1W_det_2.append(0)
            ND_time_1M_det_2.append(0)
            ND_time_3M_det_2.append(0)
            ND_time_6M_det_2.append(0)
            ND_time_1Y_det_2.append(0)
            ND_time_2Y_det_2.append(0)
            ND_time_3Y_det_2.append(0)
            ND_time_4Y_det_2.append(0)

        if patient_time_array[i] == "before":
            ND_time_before_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "1W":
            ND_time_1W_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "1M":
            ND_time_1M_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "3M":
            ND_time_3M_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "6M":
            ND_time_6M_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "1Y":
            ND_time_1Y_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "2Y":
            ND_time_2Y_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "3Y":
            ND_time_3Y_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
        elif patient_time_array[i] == "4Y":
            ND_time_4Y_det_2[ND_patient_counter_det_2] = patient_determinator_2[i]
                
# print(max_det_2)
# print(min_det_2)

D_data_det_2 = {'Patient': D_patient_number_array_det_2, 'Before' : D_time_before_det_2, '1 Week' : D_time_1W_det_2, '1 Month' : D_time_1M_det_2, '3 Months': D_time_3M_det_2, '6 Months': D_time_6M_det_2, '1 Year': D_time_1Y_det_2, '2 Years': D_time_2Y_det_2, '3 Years':D_time_3Y_det_2, '4 Years':D_time_4Y_det_2 }
D_df_det_2 = pd.DataFrame(D_data_det_2)
D_df_det_2.to_csv('RESULTS/D_Determinant2.csv', index=False)

ND_data_det_2 = {'Patient': ND_patient_number_array_det_2, 'Before' : ND_time_before_det_2, '1 Week' : ND_time_1W_det_2, '1 Month' : ND_time_1M_det_2, '3 Months': ND_time_3M_det_2, '6 Months': ND_time_6M_det_2, '1 Year': ND_time_1Y_det_2, '2 Years': ND_time_2Y_det_2, '3 Years':ND_time_3Y_det_2, '4 Years':ND_time_4Y_det_2 }
ND_df_det_2 = pd.DataFrame(ND_data_det_2)
ND_df_det_2.to_csv('RESULTS/ND_Determinant2.csv', index=False)









# - - - - - - - - - - - - - - - - - - - - - - - - GRAPHS 
def checkImproved(before, arr):
    improved = 0
    both = 0
    avg_amount = 0
    avg_diff = 0
    avg_diff_improved = 0

    for i in range(len(before)):
        if ((before[i] != 0) and (arr[i] != 0)):
            both += 1
            avg_diff += before[i] - arr[i]

            if(arr[i] < before[i]):
                improved += 1
                avg_amount += arr[i]
                avg_diff_improved += before[i] - arr[i]

    avg_diff = avg_diff/both
    avg_diff_improved = avg_diff_improved/improved
    avg_amount = avg_amount/improved
    return both, improved, avg_amount, avg_diff, avg_diff_improved

D_both_1W, D_improved_1W, D_avg_amount_1W, D_avg_diff_1W, D_avg_diff_improved_1W = checkImproved(D_time_before_det_2, D_time_1W_det_2)
D_both_1M, D_improved_1M, D_avg_amount_1M, D_avg_diff_1M, D_avg_diff_improved_1M = checkImproved(D_time_before_det_2, D_time_1M_det_2)
D_both_3M, D_improved_3M, D_avg_amount_3M, D_avg_diff_3M, D_avg_diff_improved_3M = checkImproved(D_time_before_det_2, D_time_3M_det_2)
D_both_6M, D_improved_6M, D_avg_amount_6M, D_avg_diff_6M, D_avg_diff_improved_6M = checkImproved(D_time_before_det_2, D_time_6M_det_2)
D_both_1Y, D_improved_1Y, D_avg_amount_1Y, D_avg_diff_1Y, D_avg_diff_improved_1Y = checkImproved(D_time_before_det_2, D_time_1Y_det_2)
D_both_2Y, D_improved_2Y, D_avg_amount_2Y, D_avg_diff_2Y, D_avg_diff_improved_2Y = checkImproved(D_time_before_det_2, D_time_2Y_det_2)
D_both_3Y, D_improved_3Y, D_avg_amount_3Y, D_avg_diff_3Y, D_avg_diff_improved_3Y = checkImproved(D_time_before_det_2, D_time_3Y_det_2)
D_both_4Y, D_improved_4Y, D_avg_amount_4Y, D_avg_diff_4Y, D_avg_diff_improved_4Y = checkImproved(D_time_before_det_2, D_time_4Y_det_2)

D_improved_percentage = [D_improved_1W/D_both_1W*100, D_improved_1M/D_both_1M*100, D_improved_3M/D_both_3M*100, D_improved_6M/D_both_6M*100, D_improved_1Y/D_both_1Y*100, D_improved_2Y/D_both_2Y*100, D_improved_3Y/D_both_3Y*100, D_improved_4Y/D_both_4Y*100]
D_avg_improved_amount = [D_avg_amount_1W, D_avg_amount_1M, D_avg_amount_3M, D_avg_amount_6M, D_avg_amount_1Y, D_avg_amount_2Y, D_avg_amount_3Y, D_avg_amount_4Y]
D_num_improved = [D_improved_1W, D_improved_1M, D_improved_3M, D_improved_6M, D_improved_1Y, D_improved_2Y, D_improved_3Y, D_improved_4Y]
D_total_num = [D_both_1W, D_both_1M, D_both_3M, D_both_6M, D_both_1Y, D_both_2Y, D_both_3Y, D_both_4Y]
D_avg_diff = [D_avg_diff_1W, D_avg_diff_1M, D_avg_diff_3M, D_avg_diff_6M, D_avg_diff_1Y, D_avg_diff_2Y, D_avg_diff_3Y, D_avg_diff_4Y]
D_avg_diff_improved = [D_avg_diff_improved_1W, D_avg_diff_improved_1M, D_avg_diff_improved_3M, D_avg_diff_improved_6M, D_avg_diff_improved_1Y, D_avg_diff_improved_2Y, D_avg_diff_improved_3Y, D_avg_diff_improved_4Y]

ND_both_1W, ND_improved_1W, ND_avg_amount_1W, ND_avg_diff_1W, ND_avg_diff_improved_1W = checkImproved(ND_time_before_det_2, ND_time_1W_det_2)
ND_both_1M, ND_improved_1M, ND_avg_amount_1M, ND_avg_diff_1M, ND_avg_diff_improved_1M = checkImproved(ND_time_before_det_2, ND_time_1M_det_2)
ND_both_3M, ND_improved_3M, ND_avg_amount_3M, ND_avg_diff_3M, ND_avg_diff_improved_3M = checkImproved(ND_time_before_det_2, ND_time_3M_det_2)
ND_both_6M, ND_improved_6M, ND_avg_amount_6M, ND_avg_diff_6M, ND_avg_diff_improved_6M = checkImproved(ND_time_before_det_2, ND_time_6M_det_2)
ND_both_1Y, ND_improved_1Y, ND_avg_amount_1Y, ND_avg_diff_1Y, ND_avg_diff_improved_1Y = checkImproved(ND_time_before_det_2, ND_time_1Y_det_2)
ND_both_2Y, ND_improved_2Y, ND_avg_amount_2Y, ND_avg_diff_2Y, ND_avg_diff_improved_2Y = checkImproved(ND_time_before_det_2, ND_time_2Y_det_2)
ND_both_3Y, ND_improved_3Y, ND_avg_amount_3Y, ND_avg_diff_3Y, ND_avg_diff_improved_3Y = checkImproved(ND_time_before_det_2, ND_time_3Y_det_2)
ND_both_4Y, ND_improved_4Y, ND_avg_amount_4Y, ND_avg_diff_4Y, ND_avg_diff_improved_4Y = checkImproved(ND_time_before_det_2, ND_time_4Y_det_2)

ND_improved_percentage = [ND_improved_1W/ND_both_1W*100, ND_improved_1M/ND_both_1M*100, ND_improved_3M/ND_both_3M*100, ND_improved_6M/ND_both_6M*100, ND_improved_1Y/ND_both_1Y*100, ND_improved_2Y/ND_both_2Y*100, ND_improved_3Y/ND_both_3Y*100, ND_improved_4Y/ND_both_4Y*100]
ND_avg_improved_amount = [ND_avg_amount_1W, ND_avg_amount_1M, ND_avg_amount_3M, ND_avg_amount_6M, ND_avg_amount_1Y, ND_avg_amount_2Y, ND_avg_amount_3Y, ND_avg_amount_4Y]
ND_num_improved = [ND_improved_1W, ND_improved_1M, ND_improved_3M, ND_improved_6M, ND_improved_1Y, ND_improved_2Y, ND_improved_3Y, ND_improved_4Y]
ND_total_num = [ND_both_1W, ND_both_1M, ND_both_3M, ND_both_6M, ND_both_1Y, ND_both_2Y, ND_both_3Y, ND_both_4Y]
ND_avg_diff = [ND_avg_diff_1W, ND_avg_diff_1M, ND_avg_diff_3M, ND_avg_diff_6M, ND_avg_diff_1Y, ND_avg_diff_2Y, ND_avg_diff_3Y, ND_avg_diff_4Y]
ND_avg_diff_improved = [ND_avg_diff_improved_1W, ND_avg_diff_improved_1M, ND_avg_diff_improved_3M, ND_avg_diff_improved_6M, ND_avg_diff_improved_1Y, ND_avg_diff_improved_2Y, ND_avg_diff_improved_3Y, ND_avg_diff_improved_4Y]

avg_total_num = [(D_both_1W+ND_both_1W)/2, (D_both_1M+ND_both_1M)/2, (D_both_3M+ND_both_3M)/2, (D_both_6M+ND_both_6M)/2, (D_both_1Y+ND_both_1Y)/2, (D_both_2Y+ND_both_2Y)/2, (D_both_3Y+ND_both_3Y)/2, (D_both_4Y+ND_both_4Y)/2]



# print("3Y: " + str(ND_avg_diff_3Y))

## GENERAL GRAPH SETTINGS
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('axes', axisbelow=True)
plt.rcParams.update({'font.size': 16})

## GRAPH 1: PERCENTAGE OF PATIENTS WITH TREMOR BEFORE TREATMENT THAT IMPROVED AFTER VARIOUS TREATMENT TIMES
x = ['1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y']
x_axis = np.arange(len(x))
fig, ax1 = plt.subplots(figsize = (8,4))
plt.title('Percentage of Patients with Tremor Before Treatment that Improved\nAfter Various Treatment Times')
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.tight_layout()

ax1.bar(x_axis - 0.15, D_improved_percentage, 0.3, label = 'Treated Hand', color = 'darkblue')
ax1.bar(x_axis + 0.15, ND_improved_percentage, 0.3, label = 'Treated Hand', color = 'cornflowerblue')
ax1.set_ylabel('Percentage Improved')
ax1.set_xlabel('Time')
ax1.legend(['Treated Hand', 'Untreated Hand'], loc="upper right", prop={'size': 14})
ax1.set_ylim(0, 100)
ax2 = ax1.twinx()
ax2.plot(x, avg_total_num, color = 'red')
ax2.set_ylabel('Number of Patients')
ax2.legend(['Number of\npatients'], loc="upper center", prop={'size': 14})
ax2.set_ylim(0, 100)
plt.rcParams["figure.figsize"] = (8,4)
print("AVERAGE: " + str(np.average(D_improved_percentage)))
plt.savefig('RESULTS\GRAPHS\PercentageOfPatients.png', bbox_inches='tight', dpi=150)
## GRAPH 1: PERCENTAGE OF PATIENTS WITH TREMOR BEFORE TREATMENT THAT IMPROVED AFTER VARIOUS TREATMENT TIMES

## GRAPH 2: PERCENTAGE OF PATIENTS WITH TREMOR BEFORE TREATMENT THAT IMPROVED AFTER VARIOUS TREATMENT TIMES
fig, ax1 = plt.subplots(figsize = (8,4))
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.title('Difference Between Tremor Severity Before Treatment\nand After Various Treatment Periods')

ax1.bar(x_axis - 0.15, D_avg_diff, 0.3, label = 'Treated Hand', color = 'darkblue')
ax1.bar(x_axis + 0.15, ND_avg_diff, 0.3, label = 'Treated Hand', color = 'cornflowerblue')
ax1.set_ylabel('Difference in Tremor')
ax1.legend(['Treated Hand', 'Untreated Hand'], loc="upper right")
ax1.set_xlabel('Time')

# ax1.set_ylim(0, 100)
# ax2 = ax1.twinx()
# ax2.plot(x, D_num_improved, color = 'red')
# ax2.plot(x, ND_num_improved, color = 'green')
# ax2.set_ylabel('Number of patients total')
# ax2.legend(['Treated Hand', 'Non-Treated Hand'], loc="upper center")
# ax2.set_ylim(0, 100)
plt.xticks(x_axis, x)
plt.tight_layout()

plt.show()

## GRAPH: PERCENTAGE OF PATIENTS WITH TREMOR BEFORE TREATMENT THAT IMPROVED AFTER VARIOUS TREATMENT TIMES

# plt.rcParams["font.family"] = "Times New Roman"
# plt.rc('axes', axisbelow=True)
# plt.rcParams.update({'font.size': 12})

# plt_1 = plt.figure(figsize=(8, 4))

# plt.grid(linestyle = '-', linewidth=0.5, axis='y')
# plt.title('Percentage of Patients with Tremor Before Treatment that Improved \nAfter Various Treatment Times')

# x = ['1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y']
# x_axis = np.arange(len(x))

# # plt.bar(x_axis - 0.15, D_improved_percentage, 0.3, label = 'Treated Hand', color = 'darkblue')
# # plt.bar(x_axis + 0.15, ND_improved_percentage, 0.3, label = 'Non-Treated Hand', color = 'cornflowerblue')

# plt.bar(x_axis - 0.15, D_num_improved, 0.3, label = 'Treated Hand', color = 'darkblue')
# plt.bar(x_axis + 0.15, ND_num_improved, 0.3, label = 'Non-Treated Hand', color = 'cornflowerblue')


# plt.xticks(x_axis, x)

# plt.xlabel('Time')
# plt.ylabel('Percentage that Improved')
# plt.legend()
# plt.show()
# # - - - - - - - - - - - - - - - - - - - - - - - - END OF GRAPHS 












# # - - - - - - - - - - - - - - - - - - - - - - - - START OF "WHICH HAND?"
combined_improved_array = []
which_hand = []
combined_patient_number_array = []
dominant_hand = []

longest_array = 0

if len(D_patient_number_array_det_2) > len(ND_patient_number_array_det_2): 
    longest_array = len(D_patient_number_array_det_2)
else:
    longest_array = len(ND_patient_number_array_det_2)


D_counter = -1
ND_counter = -1

_before = 1
_1W = 7
_1M = 30
_3M = 91
_6M = 183
_1Y = 365
_2Y = 730
_3Y = 1095
_4Y = 1460

_before_linear = 1
_1W_linear = 2
_1M_linear = 3
_3M_linear = 4
_6M_linear = 5
_1Y_linear = 6
_2Y_linear = 7
_3Y_linear = 8
_4Y_linear = 9

fig_ALLPATIENTS, ax1_ALLPATIENTS = plt.subplots(figsize = (8,4))

for i in range(0, longest_array):
    D_counter += 1
    ND_counter += 1
    
    if D_counter >= len(D_patient_number_array_det_2) or ND_counter >= len(ND_patient_number_array_det_2):
        break
    else:
        while D_patient_number_array_det_2[D_counter] != ND_patient_number_array_det_2[ND_counter]:
            if D_patient_number_array_det_2[D_counter+1] == ND_patient_number_array_det_2[ND_counter]:
                D_counter += 1
            elif D_patient_number_array_det_2[D_counter] == ND_patient_number_array_det_2[ND_counter + 1]:
                ND_counter += 1
            else:
                D_counter += 1
                ND_counter += 1
            
    D_x_array = []
    D_x_array_linear = []
    D_y_array = []

    if D_time_before_det_2[D_counter] != 0 and D_time_before_det_2[D_counter] != -1:
        D_y_array.append(D_time_before_det_2[D_counter])
        D_x_array.append(_before)
        D_x_array_linear.append(_before_linear)
    if D_time_1W_det_2[D_counter] != 0 and D_time_1W_det_2[D_counter] != -1:
        D_y_array.append(D_time_1W_det_2[D_counter])
        D_x_array.append(_1W)
        D_x_array_linear.append(_1W_linear)
    if D_time_1M_det_2[D_counter] != 0 and D_time_1M_det_2[D_counter] != -1:
        D_y_array.append(D_time_1M_det_2[D_counter])
        D_x_array.append(_1M)
        D_x_array_linear.append(_1M_linear)
    if D_time_3M_det_2[D_counter] != 0 and D_time_3M_det_2[D_counter] != -1:
        D_y_array.append(D_time_3M_det_2[D_counter])
        D_x_array.append(_3M)
        D_x_array_linear.append(_3M_linear)
    if D_time_6M_det_2[D_counter] != 0 and D_time_6M_det_2[D_counter] != -1:
        D_y_array.append(D_time_6M_det_2[D_counter])
        D_x_array.append(_6M)
        D_x_array_linear.append(_6M_linear)
    if D_time_1Y_det_2[D_counter] != 0 and D_time_1Y_det_2[D_counter] != -1:
        D_y_array.append(D_time_1Y_det_2[D_counter])
        D_x_array.append(_1Y)
        D_x_array_linear.append(_1Y_linear)
    if D_time_2Y_det_2[D_counter] != 0 and D_time_2Y_det_2[D_counter] != -1:
        D_y_array.append(D_time_2Y_det_2[D_counter])
        D_x_array.append(_2Y)
        D_x_array_linear.append(_2Y_linear)
    if D_time_3Y_det_2[D_counter] != 0 and D_time_3Y_det_2[D_counter] != -1:
        D_y_array.append(D_time_3Y_det_2[D_counter])
        D_x_array.append(_3Y)
        D_x_array_linear.append(_3Y_linear)
    if D_time_4Y_det_2[D_counter] != 0 and D_time_4Y_det_2[D_counter] != -1:
        D_y_array.append(D_time_4Y_det_2[D_counter])
        D_x_array.append(_4Y)
        D_x_array_linear.append(_4Y_linear)

    ND_x_array = []
    ND_x_array_linear = []
    ND_y_array = []
    if ND_time_before_det_2[ND_counter] != 0 and ND_time_before_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_before_det_2[ND_counter])
        ND_x_array.append(_before)
        ND_x_array_linear.append(_before_linear)
    if ND_time_1W_det_2[ND_counter] != 0 and ND_time_1W_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_1W_det_2[ND_counter])
        ND_x_array.append(_1W)
        ND_x_array_linear.append(_1W_linear)
    if ND_time_1M_det_2[ND_counter] != 0 and ND_time_1M_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_1M_det_2[ND_counter])
        ND_x_array.append(_1M)
        ND_x_array_linear.append(_1M_linear)
    if ND_time_3M_det_2[ND_counter] != 0 and ND_time_3M_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_3M_det_2[ND_counter])
        ND_x_array.append(_3M)
        ND_x_array_linear.append(_3M_linear)
    if ND_time_6M_det_2[ND_counter] != 0 and ND_time_6M_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_6M_det_2[ND_counter])
        ND_x_array.append(_6M)
        ND_x_array_linear.append(_6M_linear)
    if ND_time_1Y_det_2[ND_counter] != 0 and ND_time_1Y_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_1Y_det_2[ND_counter])
        ND_x_array.append(_1Y)
        ND_x_array_linear.append(_1Y_linear)
    if ND_time_2Y_det_2[ND_counter] != 0 and ND_time_2Y_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_2Y_det_2[ND_counter])
        ND_x_array.append(_2Y)
        ND_x_array_linear.append(_2Y_linear)
    if ND_time_3Y_det_2[ND_counter] != 0 and ND_time_3Y_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_3Y_det_2[ND_counter])
        ND_x_array.append(_3Y)
        ND_x_array_linear.append(_3Y_linear)
    if ND_time_4Y_det_2[ND_counter] != 0 and ND_time_4Y_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_4Y_det_2[ND_counter])
        ND_x_array.append(_4Y)
        ND_x_array_linear.append(_4Y_linear)

    if len(D_x_array) > 4 and len(D_y_array) > 4 and len(ND_x_array) > 4 and len(ND_y_array) > 4:

        combined_patient_number_array.append(D_patient_number_array_det_2[D_counter])

        D_gradient, D_intercept = np.polyfit(D_x_array, D_y_array, 1)
        ND_gradient, ND_intercept = np.polyfit(ND_x_array, ND_y_array, 1)

        
        # print(str(D_patient_number_array_det_2[D_counter]) + "\t" + str(i) + " - D_counter: " + str(D_counter) + "\tD: " + str(D_gradient) + "\tND_counter: " + str(ND_counter) + "\tND: " + str(ND_gradient))

        plt.title('Results of Patients\' Most Improved Hand')
        plt.grid(linestyle = '-', linewidth=0.5, axis='y')
        plt.xticks([1,2,3,4,5,6,7,8,9], ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])

        temp_D_y_array = np.array(D_y_array.copy())
        D_y_array_max = max(temp_D_y_array)
        temp_D_y_array = temp_D_y_array/D_y_array_max*100
        temp_ND_y_array = np.array(ND_y_array.copy())
        ND_y_array_max = max(temp_ND_y_array)
        temp_ND_y_array = temp_ND_y_array/ND_y_array_max*100

        # if D_time_before_det_2[D_counter] < 600 and ND_time_before_det_2[ND_counter] < 600: # To remove one outlier     

        if D_gradient < 0 and ND_gradient < 0: 
            combined_improved_array.append('BOTH')
            if D_gradient < ND_gradient: 
                which_hand.append('TREATED')
                ax1_ALLPATIENTS.plot(D_x_array_linear, temp_D_y_array)

            else:
                which_hand.append('NON-TREATED')                            
                ax1_ALLPATIENTS.plot(ND_x_array_linear, temp_ND_y_array)


        elif D_gradient < 0: 
            combined_improved_array.append('TREATED')
            which_hand.append('TREATED')
            ax1_ALLPATIENTS.plot(D_x_array_linear, temp_D_y_array)

        elif ND_gradient < 0: 
            combined_improved_array.append('NON-TREATED')
            which_hand.append('NON-TREATED')
            ax1_ALLPATIENTS.plot(ND_x_array_linear, temp_ND_y_array)

        else: 
            combined_improved_array.append('NEITHER')
            if D_gradient < ND_gradient:
                which_hand.append('TREATED')
            else:
                which_hand.append('NON-TREATED')


        
        # plt.title('Results of the Treated-Hand of Patients with more than Four Data Entries')
        # plt.grid(linestyle = '-', linewidth=0.5, axis='y')

        # plt.xticks([1,2,3,4,5,6,7,8,9], ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])

        # ax1_ALLPATIENTS.plot(D_x_array_linear, D_y_array)


        # ax1_ALLPATIENTS.bar(x_axis - 0.15, D_improved_percentage, 0.3, label = 'Treated Hand', color = 'darkblue')
        # ax1_ALLPATIENTS.bar(x_axis + 0.15, ND_improved_percentage, 0.3, label = 'Treated Hand', color = 'cornflowerblue')
        # ax1_ALLPATIENTS.set_ylabel('Percentage of patients that improved')
        # ax1_ALLPATIENTS.legend(['Treated Hand', 'Non-Treated Hand'], loc="upper right")
        # ax1_ALLPATIENTS.set_ylim(0, 100)
        # ax2_ALLPATIENTS = ax1_ALLPATIENTS.twinx()
        # ax2_ALLPATIENTS.plot(x, avg_total_num, color = 'red')
        # ax2_ALLPATIENTS.set_ylabel('Number of patients total')
        # ax2_ALLPATIENTS.legend(['Number of patients'], loc="upper center")
        # ax2_ALLPATIENTS.set_ylim(0, 100)

plt.tight_layout()

plt.show()



# # - - - - - - - - - - - - - - - - - - - - - - - - START OF "WHICH HAND?" TWO
combined_improved_array = []
which_hand = []
combined_patient_number_array = []
dominant_hand = []

longest_array = 0

if len(D_patient_number_array_det_2) > len(ND_patient_number_array_det_2): 
    longest_array = len(D_patient_number_array_det_2)
else:
    longest_array = len(ND_patient_number_array_det_2)


D_counter = -1
ND_counter = -1

_before = 1
_1W = 7
_1M = 30
_3M = 91
_6M = 183
_1Y = 365
_2Y = 730
_3Y = 1095
_4Y = 1460

_before_linear = 1
_1W_linear = 2
_1M_linear = 3
_3M_linear = 4
_6M_linear = 5
_1Y_linear = 6
_2Y_linear = 7
_3Y_linear = 8
_4Y_linear = 9

fig_ALLPATIENTS2, ax1_ALLPATIENTS2 = plt.subplots(figsize = (8,4))
plt.title('Results of Patients Whose \'Before\' Drawings are the Most Severe')
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.xticks([1,2,3,4,5,6,7,8,9], ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])

for i in range(0, longest_array):
    D_counter += 1
    ND_counter += 1
    
    if D_counter >= len(D_patient_number_array_det_2) or ND_counter >= len(ND_patient_number_array_det_2):
        break
    else:
        while D_patient_number_array_det_2[D_counter] != ND_patient_number_array_det_2[ND_counter]:
            if D_patient_number_array_det_2[D_counter+1] == ND_patient_number_array_det_2[ND_counter]:
                D_counter += 1
            elif D_patient_number_array_det_2[D_counter] == ND_patient_number_array_det_2[ND_counter + 1]:
                ND_counter += 1
            else:
                D_counter += 1
                ND_counter += 1
            
    D_x_array = []
    D_x_array_linear = []
    D_y_array = []

    
    if D_time_before_det_2[D_counter] != 0 and D_time_before_det_2[D_counter] != -1:
        D_y_array.append(D_time_before_det_2[D_counter])
        D_x_array.append(_before)
        D_x_array_linear.append(_before_linear)
        if D_time_1W_det_2[D_counter] != 0 and D_time_1W_det_2[D_counter] != -1:
            D_y_array.append(D_time_1W_det_2[D_counter])
            D_x_array.append(_1W)
            D_x_array_linear.append(_1W_linear)
        if D_time_1M_det_2[D_counter] != 0 and D_time_1M_det_2[D_counter] != -1:
            D_y_array.append(D_time_1M_det_2[D_counter])
            D_x_array.append(_1M)
            D_x_array_linear.append(_1M_linear)
        if D_time_3M_det_2[D_counter] != 0 and D_time_3M_det_2[D_counter] != -1:
            D_y_array.append(D_time_3M_det_2[D_counter])
            D_x_array.append(_3M)
            D_x_array_linear.append(_3M_linear)
        if D_time_6M_det_2[D_counter] != 0 and D_time_6M_det_2[D_counter] != -1:
            D_y_array.append(D_time_6M_det_2[D_counter])
            D_x_array.append(_6M)
            D_x_array_linear.append(_6M_linear)
        if D_time_1Y_det_2[D_counter] != 0 and D_time_1Y_det_2[D_counter] != -1:
            D_y_array.append(D_time_1Y_det_2[D_counter])
            D_x_array.append(_1Y)
            D_x_array_linear.append(_1Y_linear)
        if D_time_2Y_det_2[D_counter] != 0 and D_time_2Y_det_2[D_counter] != -1:
            D_y_array.append(D_time_2Y_det_2[D_counter])
            D_x_array.append(_2Y)
            D_x_array_linear.append(_2Y_linear)
        if D_time_3Y_det_2[D_counter] != 0 and D_time_3Y_det_2[D_counter] != -1:
            D_y_array.append(D_time_3Y_det_2[D_counter])
            D_x_array.append(_3Y)
            D_x_array_linear.append(_3Y_linear)
        if D_time_4Y_det_2[D_counter] != 0 and D_time_4Y_det_2[D_counter] != -1:
            D_y_array.append(D_time_4Y_det_2[D_counter])
            D_x_array.append(_4Y)
            D_x_array_linear.append(_4Y_linear)

    ND_x_array = []
    ND_x_array_linear = []
    ND_y_array = []
    if ND_time_before_det_2[ND_counter] != 0 and ND_time_before_det_2[ND_counter] != -1:
        ND_y_array.append(ND_time_before_det_2[ND_counter])
        ND_x_array.append(_before)
        ND_x_array_linear.append(_before_linear)

        if ND_time_1W_det_2[ND_counter] != 0 and ND_time_1W_det_2[ND_counter] != -1:
            ND_y_array.append(ND_time_1W_det_2[ND_counter])
            ND_x_array.append(_1W)
            ND_x_array_linear.append(_1W_linear)
        if ND_time_1M_det_2[ND_counter] != 0 and ND_time_1M_det_2[ND_counter] != -1:
            ND_y_array.append(ND_time_1M_det_2[ND_counter])
            ND_x_array.append(_1M)
            ND_x_array_linear.append(_1M_linear)
        if ND_time_3M_det_2[ND_counter] != 0 and ND_time_3M_det_2[ND_counter] != -1:
            ND_y_array.append(ND_time_3M_det_2[ND_counter])
            ND_x_array.append(_3M)
            ND_x_array_linear.append(_3M_linear)
        if ND_time_6M_det_2[ND_counter] != 0 and ND_time_6M_det_2[ND_counter] != -1:
            ND_y_array.append(ND_time_6M_det_2[ND_counter])
            ND_x_array.append(_6M)
            ND_x_array_linear.append(_6M_linear)
        if ND_time_1Y_det_2[ND_counter] != 0 and ND_time_1Y_det_2[ND_counter] != -1:
            ND_y_array.append(ND_time_1Y_det_2[ND_counter])
            ND_x_array.append(_1Y)
            ND_x_array_linear.append(_1Y_linear)
        if ND_time_2Y_det_2[ND_counter] != 0 and ND_time_2Y_det_2[ND_counter] != -1:
            ND_y_array.append(ND_time_2Y_det_2[ND_counter])
            ND_x_array.append(_2Y)
            ND_x_array_linear.append(_2Y_linear)
        if ND_time_3Y_det_2[ND_counter] != 0 and ND_time_3Y_det_2[ND_counter] != -1:
            ND_y_array.append(ND_time_3Y_det_2[ND_counter])
            ND_x_array.append(_3Y)
            ND_x_array_linear.append(_3Y_linear)
        if ND_time_4Y_det_2[ND_counter] != 0 and ND_time_4Y_det_2[ND_counter] != -1:
            ND_y_array.append(ND_time_4Y_det_2[ND_counter])
            ND_x_array.append(_4Y)
            ND_x_array_linear.append(_4Y_linear)


        
    if len(D_x_array) > 4 and len(D_y_array) > 4 and len(ND_x_array) > 4 and len(ND_y_array) > 4:

        combined_patient_number_array.append(D_patient_number_array_det_2[D_counter])

        D_gradient, D_intercept = np.polyfit(D_x_array, D_y_array, 1)
        ND_gradient, ND_intercept = np.polyfit(ND_x_array, ND_y_array, 1)

        
        # print(str(D_patient_number_array_det_2[D_counter]) + "\t" + str(i) + " - D_counter: " + str(D_counter) + "\tD: " + str(D_gradient) + "\tND_counter: " + str(ND_counter) + "\tND: " + str(ND_gradient))


        temp_D_y_array = np.array(D_y_array.copy())
        D_y_array_max = max(temp_D_y_array)
        temp_D_y_array = temp_D_y_array/D_y_array_max*100
        temp_ND_y_array = np.array(ND_y_array.copy())
        ND_y_array_max = max(temp_ND_y_array)
        temp_ND_y_array = temp_ND_y_array/ND_y_array_max*100

        if D_time_before_det_2[D_counter] < 600 and ND_time_before_det_2[ND_counter] < 600: # To remove one outlier     

            if D_gradient < 0 and ND_gradient < 0: 
                combined_improved_array.append('BOTH')
                if D_gradient < ND_gradient: 
                    which_hand.append('TREATED')
                    if D_y_array[0] == D_y_array_max:
                        ax1_ALLPATIENTS2.plot(D_x_array_linear, D_y_array)

                else:
                    which_hand.append('NON-TREATED')   
                    if ND_y_array[0] == ND_y_array_max:                   
                        ax1_ALLPATIENTS2.plot(ND_x_array_linear, ND_y_array)


            elif D_gradient < 0: 
                combined_improved_array.append('TREATED')
                which_hand.append('TREATED')
                if D_y_array[0] == D_y_array_max:
                    ax1_ALLPATIENTS2.plot(D_x_array_linear, D_y_array)

            elif ND_gradient < 0: 
                combined_improved_array.append('NON-TREATED')
                which_hand.append('NON-TREATED')
                if ND_y_array[0] == ND_y_array_max:
                    ax1_ALLPATIENTS2.plot(ND_x_array_linear, ND_y_array)

            else: 
                combined_improved_array.append('NEITHER')
                if D_gradient < ND_gradient:
                    which_hand.append('TREATED')
                else:
                    which_hand.append('NON-TREATED')
plt.tight_layout()

plt.show()


# # - - - - - - - - - - - - - - - - - - - - - - - - START OF "WHICH HAND?" THREE

x_array = [1,2,3,4,5,6,7,8,9]
fig_ALLPATIENTS3, ax1_ALLPATIENTS3 = plt.subplots(figsize = (8,4))
plt.title('Average Tremor Severities for Each Hand')
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.xticks(x_array, ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])

D_average_before_det_2 = np.mean(D_time_before_det_2)
D_average_1W_det_2 = np.mean(D_time_1W_det_2)
D_average_1M_det_2 = np.mean(D_time_1M_det_2)
D_average_3M_det_2 = np.mean(D_time_3M_det_2)
D_average_6M_det_2 = np.mean(D_time_6M_det_2)
D_average_1Y_det_2 = np.mean(D_time_1Y_det_2)
D_average_2Y_det_2 = np.mean(D_time_2Y_det_2)
D_average_3Y_det_2 = np.mean(D_time_3Y_det_2)
D_average_4Y_det_2 = np.mean(D_time_4Y_det_2)

ND_average_before_det_2 = np.mean(ND_time_before_det_2)
ND_average_1W_det_2 = np.mean(ND_time_1W_det_2)
ND_average_1M_det_2 = np.mean(ND_time_1M_det_2)
ND_average_3M_det_2 = np.mean(ND_time_3M_det_2)
ND_average_6M_det_2 = np.mean(ND_time_6M_det_2)
ND_average_1Y_det_2 = np.mean(ND_time_1Y_det_2)
ND_average_2Y_det_2 = np.mean(ND_time_2Y_det_2)
ND_average_3Y_det_2 = np.mean(ND_time_3Y_det_2)
ND_average_4Y_det_2 = np.mean(ND_time_4Y_det_2)

D_averages = [D_average_before_det_2, D_average_1W_det_2, D_average_1M_det_2, D_average_3M_det_2, D_average_6M_det_2, D_average_1Y_det_2, D_average_2Y_det_2, D_average_3Y_det_2, D_average_4Y_det_2]
ND_averages = [ND_average_before_det_2, ND_average_1W_det_2, ND_average_1M_det_2, ND_average_3M_det_2, ND_average_6M_det_2, ND_average_1Y_det_2, ND_average_2Y_det_2, ND_average_3Y_det_2, ND_average_4Y_det_2]

plt.legend()
ax1_ALLPATIENTS3.plot(x_array, D_averages, color = 'darkblue')
ax1_ALLPATIENTS3.plot(x_array, ND_averages, color = 'cornflowerblue')
ax1_ALLPATIENTS3.set_ylabel('Tremor Severity')
ax1_ALLPATIENTS3.set_xlabel('Time')
ax1_ALLPATIENTS3.legend(['Treated Hand', 'Untreated Hand'], loc="upper right")
plt.tight_layout()

plt.show()












# # - - - - - - - - - - - - - - - - - - - - - - - - START OF "WHICH HAND?" FOUR

x_array = [1,2,3,4,5,6,7,8,9]
fig_ALLPATIENTS4, ax1_ALLPATIENTS4 = plt.subplots(figsize = (8,4))
plt.title('Average Tremor Severities for Each Hand')
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.xticks(x_array, ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])

all_arrays = [*D_time_before_det_2, *D_time_1W_det_2, *D_time_1M_det_2, *D_time_3M_det_2, *D_time_6M_det_2, *D_time_1Y_det_2, *D_time_2Y_det_2, *D_time_3Y_det_2, *D_time_4Y_det_2, *ND_time_before_det_2, *ND_time_1W_det_2, *ND_time_1M_det_2, *ND_time_3M_det_2, *ND_time_6M_det_2, *ND_time_1Y_det_2, *ND_time_2Y_det_2, *ND_time_3Y_det_2, *ND_time_4Y_det_2]
# all_max_array = [max(D_time_before_det_2), max(D_time_1W_det_2), max(D_time_1M_det_2), max(D_time_3M_det_2), max(D_time_6M_det_2), max(D_time_1Y_det_2), max(D_time_2Y_det_2), max(D_time_3Y_det_2), max(D_time_4Y_det_2), max(*ND_time_before_det_2), max(*ND_time_1W_det_2), max(*ND_time_1M_det_2), max(ND_time_3M_det_2), max(ND_time_6M_det_2), max(ND_time_1Y_det_2), max(ND_time_2Y_det_2), max(ND_time_3Y_det_2), max(ND_time_4Y_det_2)]
all_min, q10, q90, q95, q98, q999, all_max = np.quantile(all_arrays, [0, 0.1, 0.9, 0.95, 0.98, 0.99, 1])
denom = q95 - all_min


# (x-min)/(max-min)
D_time_before_normalised = [(x - all_min)/denom for x in D_time_before_det_2]
D_time_1W_normalised = [(x - all_min)/denom for x in D_time_1W_det_2]
D_time_1M_normalised = [(x - all_min)/denom for x in D_time_1M_det_2]
D_time_3M_normalised = [(x - all_min)/denom for x in D_time_3M_det_2]
D_time_6M_normalised = [(x - all_min)/denom for x in D_time_6M_det_2]
D_time_1Y_normalised = [(x - all_min)/denom for x in D_time_1Y_det_2]
D_time_2Y_normalised = [(x - all_min)/denom for x in D_time_2Y_det_2]
D_time_3Y_normalised = [(x - all_min)/denom for x in D_time_3Y_det_2]
D_time_4Y_normalised = [(x - all_min)/denom for x in D_time_4Y_det_2]

D_times_normalised = [D_time_before_normalised, D_time_1W_normalised, D_time_1M_normalised, D_time_3M_normalised, D_time_6M_normalised,  D_time_1Y_normalised, D_time_2Y_normalised, D_time_3Y_normalised, D_time_4Y_normalised]

ND_time_before_normalised = [(x - all_min)/denom for x in ND_time_before_det_2]
ND_time_1W_normalised = [(x - all_min)/denom for x in ND_time_1W_det_2]
ND_time_1M_normalised = [(x - all_min)/denom for x in ND_time_1M_det_2]
ND_time_3M_normalised = [(x - all_min)/denom for x in ND_time_3M_det_2]
ND_time_6M_normalised = [(x - all_min)/denom for x in ND_time_6M_det_2]
ND_time_1Y_normalised = [(x - all_min)/denom for x in ND_time_1Y_det_2]
ND_time_2Y_normalised = [(x - all_min)/denom for x in ND_time_2Y_det_2]
ND_time_3Y_normalised = [(x - all_min)/denom for x in ND_time_3Y_det_2]
ND_time_4Y_normalised = [(x - all_min)/denom for x in ND_time_4Y_det_2]

D_average_before_det_2 = np.mean(D_time_before_normalised)
D_average_1W_det_2 = np.mean(D_time_1W_normalised)
D_average_1M_det_2 = np.mean(D_time_1M_normalised)
D_average_3M_det_2 = np.mean(D_time_3M_normalised)
D_average_6M_det_2 = np.mean(D_time_6M_normalised)
D_average_1Y_det_2 = np.mean(D_time_1Y_normalised)
D_average_2Y_det_2 = np.mean(D_time_2Y_normalised)
D_average_3Y_det_2 = np.mean(D_time_3Y_normalised)
D_average_4Y_det_2 = np.mean(D_time_4Y_normalised)

ND_average_before_det_2 = np.mean(ND_time_before_normalised)
ND_average_1W_det_2 = np.mean(ND_time_1W_normalised)
ND_average_1M_det_2 = np.mean(ND_time_1M_normalised)
ND_average_3M_det_2 = np.mean(ND_time_3M_normalised)
ND_average_6M_det_2 = np.mean(ND_time_6M_normalised)
ND_average_1Y_det_2 = np.mean(ND_time_1Y_normalised)
ND_average_2Y_det_2 = np.mean(ND_time_2Y_normalised)
ND_average_3Y_det_2 = np.mean(ND_time_3Y_normalised)
ND_average_4Y_det_2 = np.mean(ND_time_4Y_normalised)

D_averages = [D_average_before_det_2, D_average_1W_det_2, D_average_1M_det_2, D_average_3M_det_2, D_average_6M_det_2, D_average_1Y_det_2, D_average_2Y_det_2, D_average_3Y_det_2, D_average_4Y_det_2]
ND_averages = [ND_average_before_det_2, ND_average_1W_det_2, ND_average_1M_det_2, ND_average_3M_det_2, ND_average_6M_det_2, ND_average_1Y_det_2, ND_average_2Y_det_2, ND_average_3Y_det_2, ND_average_4Y_det_2]


plt.legend()
ax1_ALLPATIENTS4.plot(x_array, D_averages, color = 'darkblue')
ax1_ALLPATIENTS4.plot(x_array, ND_averages, color = 'cornflowerblue')
ax1_ALLPATIENTS4.set_ylabel('Tremor Severity')
ax1_ALLPATIENTS4.set_xlabel('Time')
ax1_ALLPATIENTS4.legend(['Treated Hand', 'Untreated Hand'], loc="upper right", prop={'size': 14})
plt.savefig('RESULTS\GRAPHS\AverageTremSev.png', bbox_inches='tight', dpi=150)

plt.show()


















# # TO NORMALISE THE RESULTS, USE THE BELOW CODE
# D_normalised_time_before = []
# D_normalised_time_1W = []
# D_normalised_time_1M = []
# D_normalised_time_3M = []
# D_normalised_time_6M = []
# D_normalised_time_1Y = []
# D_normalised_time_2Y = []
# D_normalised_time_3Y = []
# D_normalised_time_4Y = []

# ND_normalised_time_before = []
# ND_normalised_time_1W = []
# ND_normalised_time_1M = []
# ND_normalised_time_3M = []
# ND_normalised_time_6M = []
# ND_normalised_time_1Y = []
# ND_normalised_time_2Y = []
# ND_normalised_time_3Y = []
# ND_normalised_time_4Y = []

# denominator = float(max_det)-float(min_det)
# (x-min)/(max-min)
# for i in range(0, D_patient_counter+1):
#     if D_time_before[i] != 0:
#         D_normalised_time_before.append((float(D_time_before[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_before.append(0)
#     if D_time_1W[i] != 0:
#         D_normalised_time_1W.append((float(D_time_1W[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_1W.append(0)
#     if D_time_1M[i] != 0:
#         D_normalised_time_1M.append((float(D_time_1M[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_1M.append(0)
#     if D_time_3M[i] != 0:
#         D_normalised_time_3M.append((float(D_time_3M[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_3M.append(0)
#     if D_time_6M[i] != 0:
#         D_normalised_time_6M.append((float(D_time_6M[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_6M.append(0)
#     if D_time_1Y[i] != 0:
#         D_normalised_time_1Y.append((float(D_time_1Y[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_1Y.append(0)
#     if D_time_2Y[i] != 0:
#         D_normalised_time_2Y.append((float(D_time_2Y[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_2Y.append(0)
#     if D_time_3Y[i] != 0:
#         D_normalised_time_3Y.append((float(D_time_3Y[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_3Y.append(0)
#     if D_time_4Y[i] != 0:
#         D_normalised_time_4Y.append((float(D_time_4Y[i])-float(min_det))/denominator)
#     else:
#         D_normalised_time_4Y.append(0)


# data_normalised = {'Patient': D_patient_number_array, 'Before' : D_normalised_time_before, '1 Week' : D_normalised_time_1W, '1 Month' : D_normalised_time_1M, '3 Months': D_normalised_time_3M, '6 Months': D_normalised_time_6M, '1 Year': D_normalised_time_1Y, '2 Years': D_normalised_time_2Y, '3 Years': D_normalised_time_3Y, '4 Years': D_normalised_time_4Y }
# df_normalised = pd.DataFrame(data_normalised)
# df_normalised.to_csv('RESULTS\D_Determinant2_NORMALIZED.csv', index=False)

# for i in range(0, ND_patient_counter+1):
#     if ND_time_before[i] != 0:
#         ND_normalised_time_before.append((float(ND_time_before[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_before.append(0)
#     if ND_time_1W[i] != 0:
#         ND_normalised_time_1W.append((float(ND_time_1W[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_1W.append(0)
#     if ND_time_1M[i] != 0:
#         ND_normalised_time_1M.append((float(ND_time_1M[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_1M.append(0)
#     if ND_time_3M[i] != 0:
#         ND_normalised_time_3M.append((float(ND_time_3M[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_3M.append(0)
#     if ND_time_6M[i] != 0:
#         ND_normalised_time_6M.append((float(ND_time_6M[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_6M.append(0)
#     if ND_time_1Y[i] != 0:
#         ND_normalised_time_1Y.append((float(ND_time_1Y[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_1Y.append(0)
#     if ND_time_2Y[i] != 0:
#         ND_normalised_time_2Y.append((float(ND_time_2Y[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_2Y.append(0)
#     if ND_time_3Y[i] != 0:
#         ND_normalised_time_3Y.append((float(ND_time_3Y[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_3Y.append(0)
#     if ND_time_4Y[i] != 0:
#         ND_normalised_time_4Y.append((float(ND_time_4Y[i])-float(min_det))/denominator)
#     else:
#         ND_normalised_time_4Y.append(0)


# data_normalised = {'Patient': ND_patient_number_array, 'Before' : ND_normalised_time_before, '1 Week' : ND_normalised_time_1W, '1 Month' : ND_normalised_time_1M, '3 Months': ND_normalised_time_3M, '6 Months': ND_normalised_time_6M, '1 Year': ND_normalised_time_1Y, '2 Years': ND_normalised_time_2Y, '3 Years': ND_normalised_time_3Y, '4 Years': ND_normalised_time_4Y }
# df_normalised = pd.DataFrame(data_normalised)
# df_normalised.to_csv('RESULTS/ND_Determinant2_NORMALIZED.csv', index=False)