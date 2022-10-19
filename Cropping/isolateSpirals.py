# EIE Investigation: "Which Hand?"
# Jesse van der Merwe (1829172) and Robyn Gebbie (2127777)
# ELEN4012A 2022

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
import numpy as np
import cv2
import imutils
from imutils.object_detection import non_max_suppression
from pdf2image import convert_from_path
import glob
import os	
import tempfile

# Read in the PDFs and convert to .jpg- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
image_array = []
image_names = []
image_path = []

counter = 0
rawCount = 0
sizeErrorCountA = 0
sizeErrorCountB = 0
sizeErrorCountC = 0

with tempfile.TemporaryDirectory() as tempDir:
	print('created temporary directory', tempDir)
	for outer_foldername in glob.glob('Data/Original/*'):
		for foldername in glob.glob(outer_foldername + '/*'):
			newFolderName = foldername.replace("Original", "Cropped")
			os.makedirs(newFolderName, exist_ok = True)
			os.makedirs(newFolderName+'/DrawingA', exist_ok = True)
			os.makedirs(newFolderName+'/DrawingB', exist_ok = True)
			os.makedirs(newFolderName+'/DrawingC', exist_ok = True)
			for filename in glob.glob(foldername + '/*.pdf'):
				arrayName = os.path.basename(filename)
				arrayName = arrayName.replace(".pdf","")

				newName = filename.replace(".pdf","")
				newName = str(tempDir) + "/"+str(arrayName)

				newPath = foldername.replace("Original", "Cropped")
				image_path.append(newPath)

				def convertPDFtoJGP(originalImage,finalImage,dpi=200):
					pages = convert_from_path(originalImage, dpi)
					for page in pages:
						page.save(finalImage, 'JPEG')

				convertPDFtoJGP(filename,newName+'.jpg',150)
				image = cv2.imread(newName+'.jpg')
				image_array.append(image)
				image_names.append(arrayName)

				rawCount = rawCount + 1

cropToleranceA = 0.9
cropToleranceB = 0.95
cropToleranceC = 0.9

MidPlaneFractionX = 0.4
MidPlaneFractionY = 0.5

# Desired dimensions of Drawings A and B (square) or Drawing C (rectangle)
squareDimension = 300
rectangleDimension = 600

# Array used to save the various widths of Drawing A, to better calculate the average width
array_width = []
array_width.append(475)

# Arrays used to save the various x and y coordinates, to better calculate the average coordinates
array_xStartA = []
array_xStartA.append(140)
array_xStartB = []
array_xStartB.append(710)
array_xStartC = []
array_xStartC.append(140)
array_yEndA = []
array_yEndA.append(490)
array_yEndB = []
array_yEndB.append(490)
array_yEndC = []
array_yEndC.append(1032)

for counter,image in enumerate(image_array):
	print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
	print("Starting image ", image_names[counter])
	copied = image.copy()

	# orientedImage = utilities.fixOrientation(copied) # NOTE: This function was incorrectly orienting more PDFs than correcting 
	orientedImage = copied.copy()

	finalA = orientedImage.copy()
	finalB = orientedImage.copy()
	finalC = orientedImage.copy()
	image = orientedImage.copy()

	(total_h,total_w) = image.shape[:2]
	mask = np.zeros((total_h,total_w), np.uint8)
	# cv2.rectangle	(image,	(start_x, start_y), (end_x, end_y),		color, 	thickness)
	cv2.rectangle	(mask, 	(0, int(0.245*total_h)), 	(total_w, int(total_h*0.8)),	255, 	-1)

	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image = cv2.bitwise_and(image,mask)
	kernel = np.ones((3,3),np.uint8)
	image = cv2.erode(image,kernel,iterations = 1)
	image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)

	# Important: The EAST text requires that your input image dimensions be multiples of 32
	newW = 704
	newH = 704
	minConf = 0.8
	(H,W) = image.shape[:2]
	rW = W / float(newW)
	rH = H / float(newH)
	image = cv2.resize(image, (newW, newH))
	(H, W) = image.shape[:2]

	# Define the two output layer names for the EAST detector model -- the first is the output probabilities and the
	# second can be used to derive the bounding box coordinates of text
	layerNames = [
		"feature_fusion/Conv_7/Sigmoid",
		"feature_fusion/concat_3"]

	# Load the pre-trained EAST text detector
	net = cv2.dnn.readNet("Cropping/frozen_east_text_detection.pb")

	# Construct a blob from the image and then perform a forward pass of the model to obtain the two output layer sets
	blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),
		(123.68, 116.78, 103.94), swapRB=True, crop=False)

	net.setInput(blob)
	(scores, geometry) = net.forward(layerNames)

	# Show timing information on text prediction grab the number of rows and columns from the scores volume, then
	# initialize our set of bounding box rectangles and corresponding confidence scores
	(numRows, numCols) = scores.shape[2:4]
	rects = []
	confidences = []
	
	# Loop over the number of rows
	for y in range(0, numRows):
		# Extract the scores (probabilities), followed by geometrical data used to derive potential bounding box coordinates that surround text
		scoresData = scores[0, 0, y]
		xData0 = geometry[0, 0, y]
		xData1 = geometry[0, 1, y]
		xData2 = geometry[0, 2, y]
		xData3 = geometry[0, 3, y]
		anglesData = geometry[0, 4, y]

	# Loop over the number of columns
		for x in range(0, numCols):
			# If score does not have sufficient probability, ignore it
			if scoresData[x] < minConf:
				continue
	
			# Compute the offset factor as resulting feature maps will be 4x smaller than the input image
			(offsetX, offsetY) = (x * 4.0, y * 4.0)
	
			# Extract the rotation angle for the prediction and then compute the sin and cosine
			angle = anglesData[x]
			cos = np.cos(angle)
			sin = np.sin(angle)
	
			# Use the geometry volume to derive the width and height of the bounding box
			h = xData0[x] + xData2[x]
			w = xData1[x] + xData3[x]
	
			# Compute both the starting and ending (x, y)-coordinates for the text prediction bounding box
			endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
			endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
			startX = int(endX - w)
			startY = int(endY - h)
	
			# Add the bounding box coordinates and probability score to respective lists
			rects.append((startX, startY, endX, endY))
			confidences.append(scoresData[x])   

	# Apply non-maxima suppression to suppress weak, overlapping bounding boxes
	boxes = non_max_suppression(np.array(rects), probs=confidences)
	
	xStart = []
	xEnd = []
	yStart = []
	yEnd = []

	# Loop over the bounding boxes
	for (startX, startY, endX, endY) in boxes:
		# Scale the bounding box coordinates based on the respective ratios
		startX = int(startX * rW)
		startY = int(startY * rH)
		endX = int(endX * rW)
		endY = int(endY * rH)
	
		# Draw the bounding box on the image
		xStart.append(startX) # vector of x coords
		yStart.append(startY)
		xEnd.append(endX)
		yEnd.append(endY)

	(height,width) = finalA.shape[:2]
	orientation = 0

	# Set array position of the Drawing's to be -1 (i.e. not found)
	A_position = -1
	B_position = -1
	C_position = -1

	# If the coordinates match where a drawing should be, save that position to the corresponding drawing's X_position variable
	for i in range(0, len(xStart)):
		if xStart[i] < 400:
			if yEnd[i] < total_h/2:
				if A_position == -1:
					A_position = i
				else:
					if xEnd[i] - xStart[i] < 100:
						A_position = i
			elif yEnd[i] < 1300 and xEnd[i] < 500: 
				C_position = i
		elif yStart[i] < total_h/2:
			if B_position == -1:
				B_position = i
			else:
				if xEnd[i] - xStart[i] < 100:
					B_position = i

	# TESTING PURPOSES:
	# print("A POS: " + str(A_position) + " B POS: " + str(B_position) + " C POS: " + str(C_position))
	# print("X START: " + str(xStart) + "   X END: " + str(xEnd))
	# print("Y START: " + str(yStart) + "   Y END: " + str(yEnd))

	# In case a drawing is not found, use the average values instead
	# NOTE: THIS IS NOT REALLY WORKING AS INTENDED - should maybe look into using position of other detected shapes instead
	width = np.mean(array_width)
	xStart_A = np.mean(array_xStartA)
	xStart_B = np.mean(array_xStartB)
	xStart_C = np.mean(array_xStartC)
	yEnd_A = np.mean(array_yEndA)
	yEnd_B = np.mean(array_yEndB)
	yEnd_C = np.mean(array_yEndC)

	# Check if the drawing was found, and save the coordinates respectively
	if A_position != -1:
		xStart_A = xStart[A_position]
		yEnd_A = yEnd[A_position]
		array_xStartA.append(xStart_A)
		array_yEndA.append(yEnd_A)
	else:
		print("THERE IS NO A TEXT DETECTED - USING AVERAGE VALUES")

	if B_position != -1:
		xStart_B = xStart[B_position]
		yEnd_B = yEnd[B_position]
		array_xStartB.append(xStart_B)
		array_yEndB.append(yEnd_B)
	else:
		print("THERE IS NO B TEXT DETECTED - USING AVERAGE VALUES")

	if C_position != -1:
		xStart_C = xStart[C_position]
		yEnd_C = yEnd[C_position]
		array_xStartC.append(xStart_C)
		array_yEndC.append(yEnd_C)
	else:
		print("THERE IS NO C TEXT DETECTED - USING AVERAGE VALUES")

	# Using other detected Drawings to find better coordinates for missing Drawings
	if A_position == -1 and B_position != -1:
		xStart_A = xStart_B-total_w/2
		yEnd_A = yEnd[B_position]	

	if B_position == -1 and A_position != -1: 
		xStart_B = xStart_A*0.5 + total_w/2
		yEnd_B = yEnd[A_position]	

	if A_position == -1 and B_position == -1:
		xStart_A = xStart_C
		xStart_B = xStart_A*0.5 + total_w/2

		yEnd_A = yStart[C_position] - total_h/3
		yEnd_B = yStart[C_position] - total_h/3

	# Calculate the width of Drawing A, either with average or coordinate values
	width = (xStart_B*cropToleranceA-xStart_A)
	array_width.append(width)

	# TESTING PURPOSES:
	# print("WIDTH: " + str(width))
	# print("XSA: " + str(xStart_A) + " XSB: " + str(xStart_B) + " XSC: " + str(xStart_C))
	# print("YEA: " + str(yEnd_A) + " YEB: " + str(yEnd_B) + " YEC: " + str(yEnd_C))

	# CROPPING OUT SPIRAL A - - - - - - - - - - - #
	try:
		finalA = cv2.cvtColor(finalA, cv2.COLOR_BGR2GRAY)
		finalA = finalA[int(yEnd_A):int(yEnd_A+width), int(xStart_A):int(xStart_A + width)]
		finalA = imutils.resize(finalA, width=squareDimension)

		# (hFinalA,wFinalA) = finalA.shape[:2]
		# if hFinalA != wFinalA:
		# 	sizeErrorCountA = sizeErrorCountA + 1

		new_image_path = str(image_path[counter])+'/DrawingA/'+str(image_names[counter])+"_A"+".jpg"
		print(new_image_path)
		cv2.imwrite(new_image_path, finalA)
	except Exception as e:
		print("Unable to save to file A as image size is empty: ",str(e))

	# CROPPING OUT SPIRAL B - - - - - - - - - - - #
	try:
		finalB = cv2.cvtColor(finalB, cv2.COLOR_BGR2GRAY)
		finalB = finalB[ int(yEnd_B) : int((yEnd_B+width)), int(xStart_B*cropToleranceB): int((xStart_B+width)*cropToleranceB)]
		finalB = imutils.resize(finalB, width=squareDimension)

		# (hFinalB,wFinalB) = finalB.shape[:2]
		# if hFinalB != wFinalB*cropToleranceB:
		# 	sizeErrorCountB = sizeErrorCountB + 1

		new_image_path = str(image_path[counter])+'/DrawingB/'+str(image_names[counter])+"_B"+".jpg"
		print(new_image_path)
		cv2.imwrite(new_image_path, finalB)
	except Exception as e:
		print("Unable to save to file B as image size is empty: ",str(e))

	# CROPPING SPIRAL C - - - - - - - - - - - #
	try:
		finalC = cv2.cvtColor(finalC, cv2.COLOR_BGR2GRAY)
		finalC = finalC[ int(yEnd_C) : int(yEnd_C+0.75*width), int(xStart_C): int(xStart_B+width)]
		finalC = imutils.resize(finalC, width=rectangleDimension)

		# (hFinalC, wFinalC) = finalC.shape[:2]
		# if hFinalC != wFinalC: 
		# 	sizeErrorcountC = sizeErrorCountC + 1 
		
		new_image_path = str(image_path[counter])+'/DrawingC/'+str(image_names[counter])+"_C"+".jpg"
		print(new_image_path)
		cv2.imwrite(new_image_path, finalC)
	except Exception as e:
		print("Unable to save to file C as image size is empty: ",str(e))
	print("Finished image ", image_names[counter])

# REMOVING THE PERCENTAGE ERROR COUNT FOR NOW AS IT IS BUGGY
# countSpiralA = glob.glob(str(imagePathA)+ "*.jpg")
# countSpiralB = glob.glob(str(imagePathB)+ "*.jpg")
# countSpiralC = glob.glob(str(imagePathC)+ "*.jpg")

# countSpiralA = len(countSpiralA)
# countSpiralB = len(countSpiralB)
# countSpiralC = len(countSpiralC)

# print("Percentage of Spiral A processed:", (float(countSpiralA-sizeErrorCountA)/float(rawCount))*100)
# print("Percentage of Spiral B processed:", (float(countSpiralB-sizeErrorCountB)/float(rawCount))*100)
# print("Percentage of Spiral C processed:", (float(countSpiralC-sizeErrorCountC)/float(rawCount))*100)

# END OF CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #