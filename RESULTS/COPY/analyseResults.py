import csv
from matplotlib import pyplot as plt
import pandas as pd

# class Results(Enum):
    # N/A FILENAME = 0
    # YES PATIENT_NUMBER = 1
    # YES DOMINANT_HAND = 2
    # YES TIME_PERIOD = 3

    # YES AREA_TRAPZ = 4
    # MAX = 5
    # STDDEV = 6

    # YES AVG_AREA_TRAPZ = 7
    # AVG_AREA_MAX = 8
    # YES AVG_AREA_STDDEV = 9

    # NUM_PEAKS = 10
    # AVG_PEAK_DIST = 11

patient_number_array = []
patient_dominant_hand = []
patient_time_array = []

patient_area_trapz = []
patient_avg_area_trapz = []
patient_avg_std_dev_array = []

patient_num_peaks = []
patient_avg_peak_dist = []
patient_determinator_1 = []
patient_determinator_2 = []

with open('Area\Result\Results.csv', 'r') as theFile: 
    reader = csv.DictReader(theFile)
    for line in reader: 
        patient_number_array.append(line['PATIENT_NUMBER'])
        patient_dominant_hand.append(line['DOMINANT_HAND'])
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

new1_patient_time_array = patient_time_array.copy()
new1_patient_determinator_1 = patient_determinator_1.copy()
new1_patient_num_peaks = patient_num_peaks.copy()
new1_patient_avg_peak_dist = patient_avg_peak_dist.copy()
for i in range(0, n):
    for j in range(0, n-i-1):
        if new1_patient_determinator_1[j] > new1_patient_determinator_1[j+1]:
            temp = new1_patient_determinator_1[j]
            new1_patient_determinator_1[j] = new1_patient_determinator_1[j+1]
            new1_patient_determinator_1[j+1] = temp

            temp = new1_patient_time_array[j]
            new1_patient_time_array[j] = new1_patient_time_array[j+1]
            new1_patient_time_array[j+1] = temp

            temp = new1_patient_num_peaks[j]
            new1_patient_num_peaks[j] = new1_patient_num_peaks[j+1]
            new1_patient_num_peaks[j+1] = temp

            temp = new1_patient_avg_peak_dist[j]
            new1_patient_avg_peak_dist[j] = new1_patient_avg_peak_dist[j+1]
            new1_patient_avg_peak_dist[j+1] = temp

new2_patient_time_array = patient_time_array.copy()
new2_patient_determinator_2 = patient_determinator_2.copy()
new2_patient_num_peaks = patient_num_peaks.copy()
new2_patient_avg_peak_dist = patient_avg_peak_dist.copy()

for i in range(0, n):
    for j in range(0, n-i-1):
        if new2_patient_determinator_2[j] > new2_patient_determinator_2[j+1]:

            temp = new2_patient_determinator_2[j]
            new2_patient_determinator_2[j] = new2_patient_determinator_2[j+1]
            new2_patient_determinator_2[j+1] = temp

            temp = new2_patient_time_array[j]
            new2_patient_time_array[j] = new2_patient_time_array[j+1]
            new2_patient_time_array[j+1] = temp

            temp = new2_patient_num_peaks[j]
            new2_patient_num_peaks[j] = new2_patient_num_peaks[j+1]
            new2_patient_num_peaks[j+1] = temp

            temp = new2_patient_avg_peak_dist[j]
            new2_patient_avg_peak_dist[j] = new2_patient_avg_peak_dist[j+1]
            new2_patient_avg_peak_dist[j+1] = temp

### THE BELOW CODE WORKS BUT ALSO LIKE WTF IT'S SO LONG
D_patient_number_array = []
D_patient_number_array.append(1)
D_patient_counter = 0

D_time_before = []
D_time_1W = []
D_time_1M = []
D_time_3M = []
D_time_6M = []
D_time_1Y = []
D_time_2Y = []
D_time_3Y = []
D_time_4Y = []

D_time_before.append(0)
D_time_1W.append(0)
D_time_1M.append(0)
D_time_3M.append(0)
D_time_6M.append(0)
D_time_1Y.append(0)
D_time_2Y.append(0)
D_time_3Y.append(0)
D_time_4Y.append(0)

ND_patient_number_array = []
ND_patient_number_array.append(1)
ND_patient_counter = 0

ND_time_before = []
ND_time_1W = []
ND_time_1M = []
ND_time_3M = []
ND_time_6M = []
ND_time_1Y = []
ND_time_2Y = []
ND_time_3Y = []
ND_time_4Y = []

ND_time_before.append(0)
ND_time_1W.append(0)
ND_time_1M.append(0)
ND_time_3M.append(0)
ND_time_6M.append(0)
ND_time_1Y.append(0)
ND_time_2Y.append(0)
ND_time_3Y.append(0)
ND_time_4Y.append(0)

max_std_dev = 0.0
min_std_dev = 100.0

for i in range(0, n):    
    if float(patient_avg_std_dev_array[i]) > float(max_std_dev):
        max_std_dev = patient_avg_std_dev_array[i]

    if float(patient_avg_std_dev_array[i]) < float(min_std_dev) and float(patient_avg_std_dev_array[i]) >= float(0.0):
        min_std_dev = patient_avg_std_dev_array[i]

    if patient_dominant_hand[i] == 'True':
        if int(patient_number_array[i]) != int(D_patient_number_array[D_patient_counter]):
            D_patient_number_array.append(patient_number_array[i])
            D_patient_counter = D_patient_counter + 1 
            D_time_before.append(0)
            D_time_1W.append(0)
            D_time_1M.append(0)
            D_time_3M.append(0)
            D_time_6M.append(0)
            D_time_1Y.append(0)
            D_time_2Y.append(0)
            D_time_3Y.append(0)
            D_time_4Y.append(0)
            
        if patient_time_array[i] == "before":
            D_time_before[D_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1W":
            D_time_1W[D_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1M":
            D_time_1M[D_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "3M":
            D_time_3M[D_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "6M":
            D_time_6M[D_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1Y":
            D_time_1Y[D_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "2Y":
            D_time_2Y[D_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "3Y":
            D_time_3Y[D_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "4Y":
            D_time_4Y[D_patient_counter] = patient_avg_std_dev_array[i]
            
    else:
        if int(patient_number_array[i]) != int(ND_patient_number_array[ND_patient_counter]):
            ND_patient_number_array.append(patient_number_array[i])
            ND_patient_counter = ND_patient_counter + 1 
            ND_time_before.append(0)
            ND_time_1W.append(0)
            ND_time_1M.append(0)
            ND_time_3M.append(0)
            ND_time_6M.append(0)
            ND_time_1Y.append(0)
            ND_time_2Y.append(0)
            ND_time_3Y.append(0)
            ND_time_4Y.append(0)

        if patient_time_array[i] == "before":
            ND_time_before[ND_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1W":
            ND_time_1W[ND_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1M":
            ND_time_1M[ND_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "3M":
            ND_time_3M[ND_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "6M":
            ND_time_6M[ND_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "1Y":
            ND_time_1Y[ND_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "2Y":
            ND_time_2Y[ND_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "3Y":
            ND_time_3Y[ND_patient_counter] = patient_avg_std_dev_array[i]
        elif patient_time_array[i] == "4Y":
            ND_time_4Y[ND_patient_counter] = patient_avg_std_dev_array[i]
                
D_data = {'Patient': D_patient_number_array, 'Before' : D_time_before, '1 Week' : D_time_1W, '1 Month' : D_time_1M, '3 Months': D_time_3M, '6 Months': D_time_6M, '1 Year': D_time_1Y, '2 Years': D_time_2Y, '3 Years':D_time_3Y, '4 Years':D_time_4Y }
D_df = pd.DataFrame(D_data)
D_df.to_csv('RESULTS/D_AvgStdDev.csv', index=False)

ND_data = {'Patient': ND_patient_number_array, 'Before' : ND_time_before, '1 Week' : ND_time_1W, '1 Month' : ND_time_1M, '3 Months': ND_time_3M, '6 Months': ND_time_6M, '1 Year': ND_time_1Y, '2 Years': ND_time_2Y, '3 Years':ND_time_3Y, '4 Years':ND_time_4Y }
ND_df = pd.DataFrame(ND_data)
ND_df.to_csv('RESULTS/ND_AvgStdDev.csv', index=False)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

D_patient_number_array = []
D_patient_number_array.append(1)
D_patient_counter = 0

D_time_before = []
D_time_1W = []
D_time_1M = []
D_time_3M = []
D_time_6M = []
D_time_1Y = []
D_time_2Y = []
D_time_3Y = []
D_time_4Y = []

D_time_before.append(0)
D_time_1W.append(0)
D_time_1M.append(0)
D_time_3M.append(0)
D_time_6M.append(0)
D_time_1Y.append(0)
D_time_2Y.append(0)
D_time_3Y.append(0)
D_time_4Y.append(0)

ND_patient_number_array = []
ND_patient_number_array.append(1)
ND_patient_counter = 0

ND_time_before = []
ND_time_1W = []
ND_time_1M = []
ND_time_3M = []
ND_time_6M = []
ND_time_1Y = []
ND_time_2Y = []
ND_time_3Y = []
ND_time_4Y = []

ND_time_before.append(0)
ND_time_1W.append(0)
ND_time_1M.append(0)
ND_time_3M.append(0)
ND_time_6M.append(0)
ND_time_1Y.append(0)
ND_time_2Y.append(0)
ND_time_3Y.append(0)
ND_time_4Y.append(0)


max_area = 0.0
min_area = 100.0

for i in range(0, n):    
    if float(patient_avg_area_trapz[i]) > float(max_area):
        max_area = patient_avg_area_trapz[i]

    if float(patient_avg_area_trapz[i]) < float(min_area) and float(patient_avg_area_trapz[i]) >= float(0.0):
        min_area = patient_avg_area_trapz[i]

    if patient_dominant_hand[i] == 'True':
        if int(patient_number_array[i]) != int(D_patient_number_array[D_patient_counter]):
            D_patient_number_array.append(patient_number_array[i])
            D_patient_counter = D_patient_counter + 1 
            D_time_before.append(0)
            D_time_1W.append(0)
            D_time_1M.append(0)
            D_time_3M.append(0)
            D_time_6M.append(0)
            D_time_1Y.append(0)
            D_time_2Y.append(0)
            D_time_3Y.append(0)
            D_time_4Y.append(0)
            
        if patient_time_array[i] == "before":
            D_time_before[D_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1W":
            D_time_1W[D_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1M":
            D_time_1M[D_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "3M":
            D_time_3M[D_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "6M":
            D_time_6M[D_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1Y":
            D_time_1Y[D_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "2Y":
            D_time_2Y[D_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "3Y":
            D_time_3Y[D_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "4Y":
            D_time_4Y[D_patient_counter] = patient_avg_area_trapz[i]
            
    else:
        if int(patient_number_array[i]) != int(ND_patient_number_array[ND_patient_counter]):
            ND_patient_number_array.append(patient_number_array[i])
            ND_patient_counter = ND_patient_counter + 1 
            ND_time_before.append(0)
            ND_time_1W.append(0)
            ND_time_1M.append(0)
            ND_time_3M.append(0)
            ND_time_6M.append(0)
            ND_time_1Y.append(0)
            ND_time_2Y.append(0)
            ND_time_3Y.append(0)
            ND_time_4Y.append(0)

        if patient_time_array[i] == "before":
            ND_time_before[ND_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1W":
            ND_time_1W[ND_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1M":
            ND_time_1M[ND_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "3M":
            ND_time_3M[ND_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "6M":
            ND_time_6M[ND_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "1Y":
            ND_time_1Y[ND_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "2Y":
            ND_time_2Y[ND_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "3Y":
            ND_time_3Y[ND_patient_counter] = patient_avg_area_trapz[i]
        elif patient_time_array[i] == "4Y":
            ND_time_4Y[ND_patient_counter] = patient_avg_area_trapz[i]
                
D_data = {'Patient': D_patient_number_array, 'Before' : D_time_before, '1 Week' : D_time_1W, '1 Month' : D_time_1M, '3 Months': D_time_3M, '6 Months': D_time_6M, '1 Year': D_time_1Y, '2 Years': D_time_2Y, '3 Years':D_time_3Y, '4 Years':D_time_4Y }
D_df = pd.DataFrame(D_data)
D_df.to_csv('RESULTS/D_AreaTrapz.csv', index=False)

ND_data = {'Patient': ND_patient_number_array, 'Before' : ND_time_before, '1 Week' : ND_time_1W, '1 Month' : ND_time_1M, '3 Months': ND_time_3M, '6 Months': ND_time_6M, '1 Year': ND_time_1Y, '2 Years': ND_time_2Y, '3 Years':ND_time_3Y, '4 Years':ND_time_4Y }
ND_df = pd.DataFrame(ND_data)
ND_df.to_csv('RESULTS/ND_AreaTrapz.csv', index=False)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# WE ARE LOOKING HERE NOW! 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

D_patient_number_array = []
D_patient_number_array.append(1)
D_patient_counter = 0

D_time_before = []
D_time_1W = []
D_time_1M = []
D_time_3M = []
D_time_6M = []
D_time_1Y = []
D_time_2Y = []
D_time_3Y = []
D_time_4Y = []

D_time_before.append(0)
D_time_1W.append(0)
D_time_1M.append(0)
D_time_3M.append(0)
D_time_6M.append(0)
D_time_1Y.append(0)
D_time_2Y.append(0)
D_time_3Y.append(0)
D_time_4Y.append(0)

ND_patient_number_array = []
ND_patient_number_array.append(1)
ND_patient_counter = 0

ND_time_before = []
ND_time_1W = []
ND_time_1M = []
ND_time_3M = []
ND_time_6M = []
ND_time_1Y = []
ND_time_2Y = []
ND_time_3Y = []
ND_time_4Y = []

ND_time_before.append(0)
ND_time_1W.append(0)
ND_time_1M.append(0)
ND_time_3M.append(0)
ND_time_6M.append(0)
ND_time_1Y.append(0)
ND_time_2Y.append(0)
ND_time_3Y.append(0)
ND_time_4Y.append(0)


max_det = 0.0
min_det = 100.0

for i in range(0, n):    
    if float(patient_determinator_2[i]) > float(max_det):
        max_det = patient_determinator_2[i]

    if float(patient_determinator_2[i]) < float(min_det) and float(patient_determinator_2[i]) >= float(0.0):
        min_det = patient_determinator_2[i]

    if patient_dominant_hand[i] == 'True':
        if int(patient_number_array[i]) != int(D_patient_number_array[D_patient_counter]):
            D_patient_number_array.append(patient_number_array[i])
            D_patient_counter = D_patient_counter + 1 
            D_time_before.append(0)
            D_time_1W.append(0)
            D_time_1M.append(0)
            D_time_3M.append(0)
            D_time_6M.append(0)
            D_time_1Y.append(0)
            D_time_2Y.append(0)
            D_time_3Y.append(0)
            D_time_4Y.append(0)
            
        if patient_time_array[i] == "before":
            D_time_before[D_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "1W":
            D_time_1W[D_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "1M":
            D_time_1M[D_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "3M":
            D_time_3M[D_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "6M":
            D_time_6M[D_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "1Y":
            D_time_1Y[D_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "2Y":
            D_time_2Y[D_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "3Y":
            D_time_3Y[D_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "4Y":
            D_time_4Y[D_patient_counter] = patient_determinator_2[i]
            
    else:
        if int(patient_number_array[i]) != int(ND_patient_number_array[ND_patient_counter]):
            ND_patient_number_array.append(patient_number_array[i])
            ND_patient_counter = ND_patient_counter + 1 
            ND_time_before.append(0)
            ND_time_1W.append(0)
            ND_time_1M.append(0)
            ND_time_3M.append(0)
            ND_time_6M.append(0)
            ND_time_1Y.append(0)
            ND_time_2Y.append(0)
            ND_time_3Y.append(0)
            ND_time_4Y.append(0)

        if patient_time_array[i] == "before":
            ND_time_before[ND_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "1W":
            ND_time_1W[ND_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "1M":
            ND_time_1M[ND_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "3M":
            ND_time_3M[ND_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "6M":
            ND_time_6M[ND_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "1Y":
            ND_time_1Y[ND_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "2Y":
            ND_time_2Y[ND_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "3Y":
            ND_time_3Y[ND_patient_counter] = patient_determinator_2[i]
        elif patient_time_array[i] == "4Y":
            ND_time_4Y[ND_patient_counter] = patient_determinator_2[i]
                
print(max_det)
print(min_det)

D_data = {'Patient': D_patient_number_array, 'Before' : D_time_before, '1 Week' : D_time_1W, '1 Month' : D_time_1M, '3 Months': D_time_3M, '6 Months': D_time_6M, '1 Year': D_time_1Y, '2 Years': D_time_2Y, '3 Years':D_time_3Y, '4 Years':D_time_4Y }
D_df = pd.DataFrame(D_data)
D_df.to_csv('RESULTS/D_Determinant2.csv', index=False)

ND_data = {'Patient': ND_patient_number_array, 'Before' : ND_time_before, '1 Week' : ND_time_1W, '1 Month' : ND_time_1M, '3 Months': ND_time_3M, '6 Months': ND_time_6M, '1 Year': ND_time_1Y, '2 Years': ND_time_2Y, '3 Years':ND_time_3Y, '4 Years':ND_time_4Y }
ND_df = pd.DataFrame(ND_data)
ND_df.to_csv('RESULTS/ND_Determinant2.csv', index=False)

# - - - - - - - - - - - - - - - - - - - - - - - - GRAPHS 
def checkImproved(before, arr):
    improved = 0
    both = 0

    for i in range(len(before)):
        if ((before[i] != 0) and (arr[i] != 0)):
            both += 1
            if(arr[i] < before[i]):
                improved += 1
    return both, improved





D_both_1W, D_improved_1W = checkImproved(D_time_before, D_time_1W)
D_both_1M, D_improved_1M = checkImproved(D_time_before, D_time_1M)
D_both_3M, D_improved_3M = checkImproved(D_time_before, D_time_3M)
D_both_6M, D_improved_6M = checkImproved(D_time_before, D_time_6M)
D_both_1Y, D_improved_1Y = checkImproved(D_time_before, D_time_1Y)
D_both_2Y, D_improved_2Y = checkImproved(D_time_before, D_time_2Y)
D_both_3Y, D_improved_3Y = checkImproved(D_time_before, D_time_3Y)
D_both_4Y, D_improved_4Y = checkImproved(D_time_before, D_time_4Y)
D_improved_percentage = [D_improved_1W/D_both_1W, D_improved_1M/D_both_1M, D_improved_3M/D_both_3M, D_improved_6M/D_both_6M, D_improved_1Y/D_both_1Y, D_improved_2Y/D_both_2Y, D_improved_3Y/D_both_3Y, D_improved_4Y/D_both_4Y]

ND_both_1W, ND_improved_1W = checkImproved(D_time_before, D_time_1W)
ND_both_1M, ND_improved_1M = checkImproved(D_time_before, D_time_1M)
ND_both_3M, ND_improved_3M = checkImproved(D_time_before, D_time_3M)
ND_both_6M, ND_improved_6M = checkImproved(D_time_before, D_time_6M)
ND_both_1Y, ND_improved_1Y = checkImproved(D_time_before, D_time_1Y)
ND_both_2Y, ND_improved_2Y = checkImproved(D_time_before, D_time_2Y)
ND_both_3Y, ND_improved_3Y = checkImproved(D_time_before, D_time_3Y)
ND_both_4Y, ND_improved_4Y = checkImproved(D_time_before, D_time_4Y)
ND_improved_percentage = [ND_improved_1W/ND_both_1W, ND_improved_1M/ND_both_1M, ND_improved_3M/ND_both_3M, ND_improved_6M/ND_both_6M, ND_improved_1Y/ND_both_1Y, ND_improved_2Y/ND_both_2Y, ND_improved_3Y/ND_both_3Y, ND_improved_4Y/ND_both_4Y]

x_axis = ['1W', '1M', '3M', '6M', '1Y', '2Y', '3Y', '4Y']
plt_1 = plt.figure(figsize=(8, 4))
plt.bar(x_axis, D_improved_percentage, label = 'Dominant Hand', color = 'mediumblue')
plt.bar(x_axis, ND_improved_percentage, label = 'Non-Dominant Hand', color = 'slategrey')
plt.show()
# - - - - - - - - - - - - - - - - - - - - - - - - END OF GRAPHS 





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