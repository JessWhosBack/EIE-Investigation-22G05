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

# IMPORTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# IT SHOULD BE NOTED THAT "DOMINANT" AND "NON-DOMINANT" HAND REFERS TO "TREATED" AND "NON-TREATED" HANDS. 
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

with open('Method2/Results.csv', 'r') as theFile: 
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
                
D_data_det_2 = {'Patient': D_patient_number_array_det_2, 'Before' : D_time_before_det_2, '1 Week' : D_time_1W_det_2, '1 Month' : D_time_1M_det_2, '3 Months': D_time_3M_det_2, '6 Months': D_time_6M_det_2, '1 Year': D_time_1Y_det_2, '2 Years': D_time_2Y_det_2, '3 Years':D_time_3Y_det_2, '4 Years':D_time_4Y_det_2 }
D_df_det_2 = pd.DataFrame(D_data_det_2)
D_df_det_2.to_csv('RESULTS/D_Determinant2.csv', index=False)

ND_data_det_2 = {'Patient': ND_patient_number_array_det_2, 'Before' : ND_time_before_det_2, '1 Week' : ND_time_1W_det_2, '1 Month' : ND_time_1M_det_2, '3 Months': ND_time_3M_det_2, '6 Months': ND_time_6M_det_2, '1 Year': ND_time_1Y_det_2, '2 Years': ND_time_2Y_det_2, '3 Years':ND_time_3Y_det_2, '4 Years':ND_time_4Y_det_2 }
ND_df_det_2 = pd.DataFrame(ND_data_det_2)
ND_df_det_2.to_csv('RESULTS/ND_Determinant2.csv', index=False)

# GRAPHS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkImproved(before, arr):
    improved = 0
    both = 0
    avg_amount = 0
    avg_diff = 0
    avg_diff_improved = 0

    for i in range(len(before)):
        abs_before = abs(float(before[i]))
        abs_arr = abs(float(arr[i]))
        if (abs_before != 0) and (abs_arr != 0) and (abs_before != -1) and (abs_arr != -1):
            both += 1
            avg_diff += float(abs_before) - float(abs_arr)

            if float(abs_arr) < float(abs_before):
                improved += 1
                avg_amount += float(abs_arr)
                avg_diff_improved += float(abs_before) - float(abs_arr)

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

D_both_1W_AVG_AREA, D_improved_1W_AVG_AREA, D_avg_amount_1W_AVG_AREA, D_avg_diff_1W_AVG_AREA, D_avg_diff_improved_1W_AVG_AREA = checkImproved(D_time_before_avg_area_trapz, D_time_1W_avg_area_trapz)
D_both_1M_AVG_AREA, D_improved_1M_AVG_AREA, D_avg_amount_1M_AVG_AREA, D_avg_diff_1M_AVG_AREA, D_avg_diff_improved_1M_AVG_AREA = checkImproved(D_time_before_avg_area_trapz, D_time_1M_avg_area_trapz)
D_both_3M_AVG_AREA, D_improved_3M_AVG_AREA, D_avg_amount_3M_AVG_AREA, D_avg_diff_3M_AVG_AREA, D_avg_diff_improved_3M_AVG_AREA = checkImproved(D_time_before_avg_area_trapz, D_time_3M_avg_area_trapz)
D_both_6M_AVG_AREA, D_improved_6M_AVG_AREA, D_avg_amount_6M_AVG_AREA, D_avg_diff_6M_AVG_AREA, D_avg_diff_improved_6M_AVG_AREA = checkImproved(D_time_before_avg_area_trapz, D_time_6M_avg_area_trapz)
D_both_1Y_AVG_AREA, D_improved_1Y_AVG_AREA, D_avg_amount_1Y_AVG_AREA, D_avg_diff_1Y_AVG_AREA, D_avg_diff_improved_1Y_AVG_AREA = checkImproved(D_time_before_avg_area_trapz, D_time_1Y_avg_area_trapz)
D_both_2Y_AVG_AREA, D_improved_2Y_AVG_AREA, D_avg_amount_2Y_AVG_AREA, D_avg_diff_2Y_AVG_AREA, D_avg_diff_improved_2Y_AVG_AREA = checkImproved(D_time_before_avg_area_trapz, D_time_2Y_avg_area_trapz)
D_both_3Y_AVG_AREA, D_improved_3Y_AVG_AREA, D_avg_amount_3Y_AVG_AREA, D_avg_diff_3Y_AVG_AREA, D_avg_diff_improved_3Y_AVG_AREA = checkImproved(D_time_before_avg_area_trapz, D_time_3Y_avg_area_trapz)
D_both_4Y_AVG_AREA, D_improved_4Y_AVG_AREA, D_avg_amount_4Y_AVG_AREA, D_avg_diff_4Y_AVG_AREA, D_avg_diff_improved_4Y_AVG_AREA = checkImproved(D_time_before_avg_area_trapz, D_time_4Y_avg_area_trapz)

ND_both_1W_AVG_AREA, ND_improved_1W_AVG_AREA, ND_avg_amount_1W_AVG_AREA, ND_avg_diff_1W_AVG_AREA, ND_avg_diff_improved_1W_AVG_AREA = checkImproved(ND_time_before_avg_area_trapz, ND_time_1W_avg_area_trapz)
ND_both_1M_AVG_AREA, ND_improved_1M_AVG_AREA, ND_avg_amount_1M_AVG_AREA, ND_avg_diff_1M_AVG_AREA, ND_avg_diff_improved_1M_AVG_AREA = checkImproved(ND_time_before_avg_area_trapz, ND_time_1M_avg_area_trapz)
ND_both_3M_AVG_AREA, ND_improved_3M_AVG_AREA, ND_avg_amount_3M_AVG_AREA, ND_avg_diff_3M_AVG_AREA, ND_avg_diff_improved_3M_AVG_AREA = checkImproved(ND_time_before_avg_area_trapz, ND_time_3M_avg_area_trapz)
ND_both_6M_AVG_AREA, ND_improved_6M_AVG_AREA, ND_avg_amount_6M_AVG_AREA, ND_avg_diff_6M_AVG_AREA, ND_avg_diff_improved_6M_AVG_AREA = checkImproved(ND_time_before_avg_area_trapz, ND_time_6M_avg_area_trapz)
ND_both_1Y_AVG_AREA, ND_improved_1Y_AVG_AREA, ND_avg_amount_1Y_AVG_AREA, ND_avg_diff_1Y_AVG_AREA, ND_avg_diff_improved_1Y_AVG_AREA = checkImproved(ND_time_before_avg_area_trapz, ND_time_1Y_avg_area_trapz)
ND_both_2Y_AVG_AREA, ND_improved_2Y_AVG_AREA, ND_avg_amount_2Y_AVG_AREA, ND_avg_diff_2Y_AVG_AREA, ND_avg_diff_improved_2Y_AVG_AREA = checkImproved(ND_time_before_avg_area_trapz, ND_time_2Y_avg_area_trapz)
ND_both_3Y_AVG_AREA, ND_improved_3Y_AVG_AREA, ND_avg_amount_3Y_AVG_AREA, ND_avg_diff_3Y_AVG_AREA, ND_avg_diff_improved_3Y_AVG_AREA = checkImproved(ND_time_before_avg_area_trapz, ND_time_3Y_avg_area_trapz)
ND_both_4Y_AVG_AREA, ND_improved_4Y_AVG_AREA, ND_avg_amount_4Y_AVG_AREA, ND_avg_diff_4Y_AVG_AREA, ND_avg_diff_improved_4Y_AVG_AREA = checkImproved(ND_time_before_avg_area_trapz, ND_time_4Y_avg_area_trapz)

D_improved_percentage_AVG_AREA = [D_improved_1W_AVG_AREA/D_both_1W_AVG_AREA*100, D_improved_1M_AVG_AREA/D_both_1M_AVG_AREA*100, D_improved_3M_AVG_AREA/D_both_3M_AVG_AREA*100, D_improved_6M_AVG_AREA/D_both_6M_AVG_AREA*100, D_improved_1Y_AVG_AREA/D_both_1Y_AVG_AREA*100, D_improved_2Y_AVG_AREA/D_both_2Y_AVG_AREA*100, D_improved_3Y_AVG_AREA/D_both_3Y_AVG_AREA*100, D_improved_4Y_AVG_AREA/D_both_4Y_AVG_AREA*100]
ND_improved_percentage_AVG_AREA = [ND_improved_1W_AVG_AREA/ND_both_1W_AVG_AREA*100, ND_improved_1M_AVG_AREA/ND_both_1M_AVG_AREA*100, ND_improved_3M_AVG_AREA/ND_both_3M_AVG_AREA*100, ND_improved_6M_AVG_AREA/ND_both_6M_AVG_AREA*100, ND_improved_1Y_AVG_AREA/ND_both_1Y_AVG_AREA*100, ND_improved_2Y_AVG_AREA/ND_both_2Y_AVG_AREA*100, ND_improved_3Y_AVG_AREA/ND_both_3Y_AVG_AREA*100, ND_improved_4Y_AVG_AREA/ND_both_4Y_AVG_AREA*100]

## GENERAL GRAPH SETTINGS
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('axes', axisbelow=True)
plt.rcParams.update({'font.size': 16})

## GRAPH 1: PERCENTAGE OF PATIENTS WITH TREMOR BEFORE TREATMENT THAT IMPROVED AFTER VARIOUS TREATMENT TIMES
x = ['1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y']
x_axis = np.arange(len(x))
fig, ax1 = plt.subplots(figsize = (8,4))
plt.title('Percentage of Patients with Tremor Before Treatment that Improved\nAfter Various Treatment Times - PEAK DISTANCE (METHOD 2B)')
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
print("AVERAGE PEAK DISTANCE DOMINANT: " + str(np.average(D_improved_percentage)))
print("AVERAGE PEAK DISTANCE NON-DOMINANT: " + str(np.average(ND_improved_percentage)))
plt.savefig('RESULTS\GRAPHS\PercentageOfPatients_Det2.png', bbox_inches='tight', dpi=150)

## GRAPH 2: PERCENTAGE OF PATIENTS WITH TREMOR BEFORE TREATMENT THAT IMPROVED AFTER VARIOUS TREATMENT TIMES
fig, ax1 = plt.subplots(figsize = (8,4))
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.title('Difference Between Tremor Severity Before Treatment\nand After Various Treatment Periods')

ax1.bar(x_axis - 0.15, D_avg_diff, 0.3, label = 'Treated Hand', color = 'darkblue')
ax1.bar(x_axis + 0.15, ND_avg_diff, 0.3, label = 'Treated Hand', color = 'cornflowerblue')
ax1.set_ylabel('Difference in Tremor')
ax1.legend(['Treated Hand', 'Untreated Hand'], loc="upper right")
ax1.set_xlabel('Time')

plt.xticks(x_axis, x)
plt.tight_layout()
plt.show()

## GRAPH 3: PERCENTAGE OF PATIENTS WITH TREMOR BEFORE TREATMENT THAT IMPROVED AFTER VARIOUS TREATMENT TIMES - AVG AREA
x = ['1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y']
x_axis = np.arange(len(x))
fig, ax1 = plt.subplots(figsize = (8,4))
plt.title('Percentage of Patients with Tremor Before Treatment that Improved\nAfter Various Treatment Times - AVERAGE AREA (METHOD 2A)')
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.tight_layout()

ax1.bar(x_axis - 0.15, D_improved_percentage_AVG_AREA, 0.3, label = 'Treated Hand', color = 'darkblue')
ax1.bar(x_axis + 0.15, ND_improved_percentage_AVG_AREA, 0.3, label = 'Treated Hand', color = 'cornflowerblue')
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
print("AVERAGE AREA METHOD DOM: " + str(np.average(D_improved_percentage_AVG_AREA)))
print("AVERAGE AREA METHOD NON-DOM: " + str(np.average(ND_improved_percentage_AVG_AREA)))
plt.savefig('RESULTS\GRAPHS\PercentageOfPatients_AvgArea.png', bbox_inches='tight', dpi=150)

# START OF "WHICH HAND?" ONE
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

        plt.title('Results of Patients\' Most Improved Hand')
        plt.grid(linestyle = '-', linewidth=0.5, axis='y')
        plt.xticks([1,2,3,4,5,6,7,8,9], ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])

        temp_D_y_array = np.array(D_y_array.copy())
        D_y_array_max = max(temp_D_y_array)
        temp_D_y_array = temp_D_y_array/D_y_array_max*100
        temp_ND_y_array = np.array(ND_y_array.copy())
        ND_y_array_max = max(temp_ND_y_array)
        temp_ND_y_array = temp_ND_y_array/ND_y_array_max*100

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

plt.tight_layout()
plt.show()

# START OF "WHICH HAND?" TWO
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

# START OF "WHICH HAND?" THREE
x_array = [1,2,3,4,5,6,7,8,9]
fig_ALLPATIENTS3, ax1_ALLPATIENTS3 = plt.subplots(figsize = (8,4))
plt.title('Average Tremor Severities for Each Hand\nPEAK DISTANCE (METHOD 2B)')
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

# AVERAGE TREMOR SEVERITY USING AVG AREA TRAPZ METHOD
x_array = [1,2,3,4,5,6,7,8,9]
fig_ALLPATIENTS3B, ax1_ALLPATIENTS3B = plt.subplots(figsize = (8,4))
plt.title('Average Tremor Severities for Each Hand\nAVERAGE AREA (METHOD 2A)')
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.xticks(x_array, ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])

D_average_before_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_before_avg_area_trapz])
D_average_1W_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_1W_avg_area_trapz])
D_average_1M_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_1M_avg_area_trapz])
D_average_3M_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_3M_avg_area_trapz])
D_average_6M_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_6M_avg_area_trapz])
D_average_1Y_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_1Y_avg_area_trapz])
D_average_2Y_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_2Y_avg_area_trapz])
D_average_3Y_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_3Y_avg_area_trapz])
D_average_4Y_avg_area_trapz = np.mean([abs(float(x)) for x in D_time_4Y_avg_area_trapz])

ND_average_before_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_before_avg_area_trapz])
ND_average_1W_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_1W_avg_area_trapz])
ND_average_1M_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_1M_avg_area_trapz])
ND_average_3M_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_3M_avg_area_trapz])
ND_average_6M_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_6M_avg_area_trapz])
ND_average_1Y_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_1Y_avg_area_trapz])
ND_average_2Y_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_2Y_avg_area_trapz])
ND_average_3Y_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_3Y_avg_area_trapz])
ND_average_4Y_avg_area_trapz = np.mean([abs(float(x)) for x in ND_time_4Y_avg_area_trapz])

D_averages = [D_average_before_avg_area_trapz, D_average_1W_avg_area_trapz, D_average_1M_avg_area_trapz, D_average_3M_avg_area_trapz, D_average_6M_avg_area_trapz, D_average_1Y_avg_area_trapz, D_average_2Y_avg_area_trapz, D_average_3Y_avg_area_trapz, D_average_4Y_avg_area_trapz]
ND_averages = [ND_average_before_avg_area_trapz, ND_average_1W_avg_area_trapz, ND_average_1M_avg_area_trapz, ND_average_3M_avg_area_trapz, ND_average_6M_avg_area_trapz, ND_average_1Y_avg_area_trapz, ND_average_2Y_avg_area_trapz, ND_average_3Y_avg_area_trapz, ND_average_4Y_avg_area_trapz]

plt.legend()
ax1_ALLPATIENTS3B.plot(x_array, D_averages, color = 'darkblue')
ax1_ALLPATIENTS3B.plot(x_array, ND_averages, color = 'cornflowerblue')
ax1_ALLPATIENTS3B.set_ylabel('Tremor Severity')
ax1_ALLPATIENTS3B.set_xlabel('Time')
ax1_ALLPATIENTS3B.legend(['Treated Hand', 'Untreated Hand'], loc="upper right")
plt.savefig('RESULTS\GRAPHS\AverageTremSev_AvgArea.png', bbox_inches='tight', dpi=150)

plt.tight_layout()
plt.show()

# START OF "WHICH HAND?" FOUR

x_array = [1,2,3,4,5,6,7,8,9]
fig_ALLPATIENTS4, ax1_ALLPATIENTS4 = plt.subplots(figsize = (8,4))
plt.title('Normalised Average Tremor Severities for Each Hand\nPEAK DISTANCE (METHOD 2B)')
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.xticks(x_array, ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])

all_arrays = [*D_time_before_det_2, *D_time_1W_det_2, *D_time_1M_det_2, *D_time_3M_det_2, *D_time_6M_det_2, *D_time_1Y_det_2, *D_time_2Y_det_2, *D_time_3Y_det_2, *D_time_4Y_det_2, *ND_time_before_det_2, *ND_time_1W_det_2, *ND_time_1M_det_2, *ND_time_3M_det_2, *ND_time_6M_det_2, *ND_time_1Y_det_2, *ND_time_2Y_det_2, *ND_time_3Y_det_2, *ND_time_4Y_det_2]
all_min, q10, q90, q95, q98, q999, all_max = np.quantile(all_arrays, [0, 0.1, 0.9, 0.95, 0.98, 0.99, 1])
denom = q95 - all_min

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
plt.savefig('RESULTS\GRAPHS\AverageTremSev_Det2.png', bbox_inches='tight', dpi=150)
plt.show()

# START OF "WHICH HAND?" FOUR B
x_array = [1,2,3,4,5,6,7,8,9]
fig_ALLPATIENTS4B, ax1_ALLPATIENTS4B = plt.subplots(figsize = (8,4))
plt.title('Normalised Average Tremor Severities for Each Hand\nAVERAGE AREA (METHOD 2A)')
plt.grid(linestyle = '-', linewidth=0.5, axis='y')
plt.xticks(x_array, ['Before', '1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y'])


copy_D_time_before_avg_area_trapz = [abs(float(x)) for x in D_time_before_avg_area_trapz]
for c in copy_D_time_before_avg_area_trapz:
    if c == 0.0:
        copy_D_time_before_avg_area_trapz.remove(c)
copy_D_time_1W_avg_area_trapz = [abs(float(x)) for x in D_time_1W_avg_area_trapz]
for c in copy_D_time_1W_avg_area_trapz:
    if c == 0.0:
        copy_D_time_1W_avg_area_trapz.remove(c)
copy_D_time_1M_avg_area_trapz = [abs(float(x)) for x in D_time_1M_avg_area_trapz]
for c in copy_D_time_1M_avg_area_trapz:
    if c == 0.0:
        copy_D_time_1M_avg_area_trapz.remove(c)
copy_D_time_3M_avg_area_trapz = [abs(float(x)) for x in D_time_3M_avg_area_trapz]
for c in copy_D_time_3M_avg_area_trapz:
    if c == 0.0:
        copy_D_time_3M_avg_area_trapz.remove(c)
copy_D_time_6M_avg_area_trapz = [abs(float(x)) for x in D_time_6M_avg_area_trapz]
for c in copy_D_time_6M_avg_area_trapz:
    if c == 0.0:
        copy_D_time_6M_avg_area_trapz.remove(c)
copy_D_time_1Y_avg_area_trapz = [abs(float(x)) for x in D_time_1Y_avg_area_trapz]
for c in copy_D_time_1Y_avg_area_trapz:
    if c == 0.0:
        copy_D_time_1Y_avg_area_trapz.remove(c)
copy_D_time_2Y_avg_area_trapz = [abs(float(x)) for x in D_time_2Y_avg_area_trapz]
for c in copy_D_time_2Y_avg_area_trapz:
    if c == 0.0:
        copy_D_time_2Y_avg_area_trapz.remove(c)
copy_D_time_3Y_avg_area_trapz = [abs(float(x)) for x in D_time_3Y_avg_area_trapz]
for c in copy_D_time_3Y_avg_area_trapz:
    if c == 0.0:
        copy_D_time_3Y_avg_area_trapz.remove(c)
copy_D_time_4Y_avg_area_trapz = [abs(float(x)) for x in D_time_4Y_avg_area_trapz]
for c in copy_D_time_4Y_avg_area_trapz:
    if c == 0.0:
        copy_D_time_4Y_avg_area_trapz.remove(c)


copy_ND_time_before_avg_area_trapz = [abs(float(x)) for x in ND_time_before_avg_area_trapz]
for c in copy_ND_time_before_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_before_avg_area_trapz.remove(c)
copy_ND_time_1W_avg_area_trapz = [abs(float(x)) for x in ND_time_1W_avg_area_trapz]
for c in copy_ND_time_1W_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_1W_avg_area_trapz.remove(c)
copy_ND_time_1M_avg_area_trapz = [abs(float(x)) for x in ND_time_1M_avg_area_trapz]
for c in copy_ND_time_1M_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_1M_avg_area_trapz.remove(c)
copy_ND_time_3M_avg_area_trapz = [abs(float(x)) for x in ND_time_3M_avg_area_trapz]
for c in copy_ND_time_3M_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_3M_avg_area_trapz.remove(c)
copy_ND_time_6M_avg_area_trapz = [abs(float(x)) for x in ND_time_6M_avg_area_trapz]
for c in copy_ND_time_6M_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_6M_avg_area_trapz.remove(c)
copy_ND_time_1Y_avg_area_trapz = [abs(float(x)) for x in ND_time_1Y_avg_area_trapz]
for c in copy_ND_time_1Y_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_1Y_avg_area_trapz.remove(c)
copy_ND_time_2Y_avg_area_trapz = [abs(float(x)) for x in ND_time_2Y_avg_area_trapz]
for c in copy_ND_time_2Y_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_2Y_avg_area_trapz.remove(c)
copy_ND_time_3Y_avg_area_trapz = [abs(float(x)) for x in ND_time_3Y_avg_area_trapz]
for c in copy_ND_time_3Y_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_3Y_avg_area_trapz.remove(c)
copy_ND_time_4Y_avg_area_trapz = [abs(float(x)) for x in ND_time_4Y_avg_area_trapz]
for c in copy_ND_time_4Y_avg_area_trapz:
    if c == 0.0:
        copy_ND_time_4Y_avg_area_trapz.remove(c)

print(copy_D_time_before_avg_area_trapz)
print(copy_ND_time_before_avg_area_trapz)
m1 = max(copy_D_time_before_avg_area_trapz)
m2 = max(copy_D_time_1W_avg_area_trapz)
m3 = max(copy_D_time_1M_avg_area_trapz)
m4 = max(copy_D_time_3M_avg_area_trapz)
m5 = max(copy_D_time_6M_avg_area_trapz)
m6 = max(copy_D_time_1Y_avg_area_trapz )
m7 = max(copy_D_time_2Y_avg_area_trapz )
m8 = max(copy_D_time_3Y_avg_area_trapz )
m9 = max(copy_D_time_4Y_avg_area_trapz )

m10 = max(copy_ND_time_before_avg_area_trapz)
m11 = max(copy_ND_time_1W_avg_area_trapz)
m12 = max(copy_ND_time_1M_avg_area_trapz)
m13 = max(copy_ND_time_3M_avg_area_trapz)
m14 = max(copy_ND_time_6M_avg_area_trapz)
m15 = max(copy_ND_time_1Y_avg_area_trapz)
m16 = max(copy_ND_time_2Y_avg_area_trapz)
m17 = max(copy_ND_time_3Y_avg_area_trapz)
m18 = max(copy_ND_time_4Y_avg_area_trapz)

m1 = min(copy_D_time_before_avg_area_trapz)
m2 = min(copy_D_time_1W_avg_area_trapz)
m3 = min(copy_D_time_1M_avg_area_trapz)
m4 = min(copy_D_time_3M_avg_area_trapz)
m5 = min(copy_D_time_6M_avg_area_trapz)
m6 = min(copy_D_time_1Y_avg_area_trapz )
m7 = min(copy_D_time_2Y_avg_area_trapz )
m8 = min(copy_D_time_3Y_avg_area_trapz )
m9 = min(copy_D_time_4Y_avg_area_trapz )

m10 = min(copy_ND_time_before_avg_area_trapz)
m11 = min(copy_ND_time_1W_avg_area_trapz)
m12 = min(copy_ND_time_1M_avg_area_trapz)
m13 = min(copy_ND_time_3M_avg_area_trapz)
m14 = min(copy_ND_time_6M_avg_area_trapz)
m15 = min(copy_ND_time_1Y_avg_area_trapz)
m16 = min(copy_ND_time_2Y_avg_area_trapz)
m17 = min(copy_ND_time_3Y_avg_area_trapz)
m18 = min(copy_ND_time_4Y_avg_area_trapz)

actual_max = max(m1, m2, m3, m4, m5, m6, m7, m8, m9, m11, m12, m13, m14, m15, m16, m17, m18)
all_min = min(m1, m2, m3, m4, m5, m6, m7, m8, m9, m11, m12, m13, m14, m15, m16, m17, m18)

# all_arrays = [*([abs(float(x)) for x in copy_D_time_before_avg_area_trapz]),*([abs(float(x)) for x in copy_D_time_1W_avg_area_trapz]),*([abs(float(x)) for x in copy_D_time_1M_avg_area_trapz]),*([abs(float(x)) for x in copy_D_time_3M_avg_area_trapz]),*([abs(float(x)) for x in copy_D_time_6M_avg_area_trapz]),*([abs(float(x)) for x in copy_D_time_1Y_avg_area_trapz]),*([abs(float(x)) for x in copy_D_time_2Y_avg_area_trapz]),*([abs(float(x)) for x in copy_D_time_3Y_avg_area_trapz]),*([abs(float(x)) for x in copy_D_time_4Y_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_before_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_1W_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_1M_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_3M_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_6M_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_1Y_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_2Y_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_3Y_avg_area_trapz]),*([abs(float(x)) for x in copy_ND_time_4Y_avg_area_trapz])]
# all_min, q10, q90, q95, q98, q99, q999, all_max = np.quantile(all_arrays, [0, 0.1, 0.9, 0.95, 0.98, 0.99, 0.999, 1])

# NB: BUG WARNING HERE - WHY IS MAX 0?
denom = 50 # actual_max - all_min

D_time_before_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_D_time_before_avg_area_trapz]]
D_time_1W_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in  copy_D_time_1W_avg_area_trapz]]
D_time_1M_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_D_time_1M_avg_area_trapz]]
D_time_3M_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_D_time_3M_avg_area_trapz]]
D_time_6M_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_D_time_6M_avg_area_trapz]]
D_time_1Y_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_D_time_1Y_avg_area_trapz]]
D_time_2Y_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_D_time_2Y_avg_area_trapz]]
D_time_3Y_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_D_time_3Y_avg_area_trapz]]
D_time_4Y_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_D_time_4Y_avg_area_trapz]]

D_times_normalised = [D_time_before_normalised, D_time_1W_normalised, D_time_1M_normalised, D_time_3M_normalised, D_time_6M_normalised,  D_time_1Y_normalised, D_time_2Y_normalised, D_time_3Y_normalised, D_time_4Y_normalised]

ND_time_before_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_before_avg_area_trapz]]
ND_time_1W_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_1W_avg_area_trapz]]
ND_time_1M_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_1M_avg_area_trapz]]
ND_time_3M_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_3M_avg_area_trapz]]
ND_time_6M_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_6M_avg_area_trapz]]
ND_time_1Y_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_1Y_avg_area_trapz]]
ND_time_2Y_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_2Y_avg_area_trapz]]
ND_time_3Y_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_3Y_avg_area_trapz]]
ND_time_4Y_normalised = [(x - all_min)/denom for x in [abs(float(x)) for x in copy_ND_time_4Y_avg_area_trapz]]

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
ax1_ALLPATIENTS4B.plot(x_array, D_averages, color = 'darkblue')
ax1_ALLPATIENTS4B.plot(x_array, ND_averages, color = 'cornflowerblue')
ax1_ALLPATIENTS4B.set_ylabel('Tremor Severity')
ax1_ALLPATIENTS4B.set_xlabel('Time')
ax1_ALLPATIENTS4B.legend(['Treated Hand', 'Untreated Hand'], loc="upper right", prop={'size': 14})
plt.savefig('RESULTS\GRAPHS\AverageTremSev_AvgArea.png', bbox_inches='tight', dpi=150)
plt.show()

# END OF CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #