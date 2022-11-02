# EIE Investigation: "Which Hand?"
# Jesse van der Merwe (1829172) and Robyn Gebbie (2127777)
# ELEN4012A NOVEMBER 2022

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# COPYRIGHT NOTICE: 
# This code contains snippets from Adrian Rosebrock's article "OpenCV shape detection" (08/02/2016) 
# Which can be found at: https://pyimagesearch.com/2016/02/08/opencv-shape-detection/ 
# 
# This code also contains snippets from jdhao's article "Cropping Rotated Rectangles from Image with OpenCV" (23/02/2019)
# Which can be found at: https://jdhao.github.io/2019/02/23/crop_rotated_rectangle_opencv/
# 
# It has further been modified and combined to suit the needs of this project.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# IMPORTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
import imutils
import cv2
import glob
import os	
from PIL import Image
import numpy as np

# Read in the .jpgs and save into an image array- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
image_array = []
image_names = []
image_path = []

for outer_foldername in glob.glob('Data\Cropped\*'):
    for foldername in glob.glob(outer_foldername + '\*'):
        for filename in glob.glob(foldername + "\DrawingC\*.jpg"):
            im = Image.open(filename).convert('L') # convert image to grayscale
            res = im.point((lambda p: 256 if p>=200 else 0)) # convert each pixel into either black or white
            res.save(filename)

            arrayName = os.path.basename(filename)
            arrayName = arrayName.replace(".jpg","")

            newPath = foldername + '\DrawingC\Rectangles'
            os.makedirs(newPath, exist_ok = True)
            image_path.append(newPath)

            image = cv2.imread(filename)
            image = cv2.bitwise_not(image) # invert the colors of the image
            image_array.append(image)
            image_names.append(arrayName)

# Loop through the image array and extract the top-most hand drawn rectangle- - - - - - - - - - - - - - - - - - - - - - - #
for image_counter,images in enumerate(image_array):
    image = images.copy()
    ratio = image.shape[0] / float(image.shape[0])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]

    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    coordinate_1 = []
    coordinate_2 = []
    coordinate_3 = []
    coordinate_4 = []

    for c in contours:
        if cv2.contourArea(c) > 50:
            try:
                x1, y1, w, h = cv2.boundingRect(c)
                if w > 350:
                    M = cv2.moments(c)
                    cX = int((M["m10"] / M["m00"]) * ratio)
                    cY = int((M["m01"] / M["m00"]) * ratio)

                    # multiply the contour (x, y)-coordinates by the resize ratio
                    c = c.astype("float")
                    c *= ratio
                    c = c.astype("int")
                    
                    rect = cv2.minAreaRect(c)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)

                    b_counter = 0
                    b_left_1 = -1
                    b_left_2 = -1
                    b_right_1 = -1
                    b_right_2 = -1

                    # Sort the boxes so that the coordinates are in the correct order (top-left, top-right, bottom-right, bottom-left)
                    for b in box: 
                        if b[0] < 100: 
                            if b_left_1 == -1:
                                b_left_1 = b_counter
                            else:
                                b_left_2 = b_counter
                        else: 
                            if b_right_1 == -1:
                                b_right_1 = b_counter
                            else:
                                b_right_2 = b_counter

                        b_counter = b_counter + 1

                    if box[b_left_1][1] < box[b_left_2][1]:
                        coordinate_1.append(box[b_left_1])
                        coordinate_4.append(box[b_left_2])
                    else:
                        coordinate_1.append(box[b_left_2])
                        coordinate_4.append(box[b_left_1])                   

                    if box[b_right_1][1] < box[b_right_2][1]:
                        coordinate_2.append(box[b_right_1])
                        coordinate_3.append(box[b_right_2])
                    else: 
                        coordinate_2.append(box[b_right_2])
                        coordinate_3.append(box[b_right_1])
            except:
                print("ERROR")

    try:
        counter = 0
        number_boxes = len(coordinate_1)

        # Since we detected the black surrounding boxes, we can now work out the coordinates of the inner drawing
        new_coordinate_1 = coordinate_4[number_boxes-1] # top box's bottom-left (4th) coordinate becomes the new top-left (1st)
        new_coordinate_2 = coordinate_3[number_boxes-1] # top box's bottom-right (3rd) coordinate becomes the new top-right (2nd)
        new_coordinate_3 = coordinate_2[number_boxes-2] # bottom box's top-right (2nd) coordinate becomes the new bottom-right (3rd)
        new_coordinate_4 = coordinate_1[number_boxes-2] # bottom box's top-left (1st) coordinate becomes the new bottom-left (4th)

        new_coordinate_array = np.array([
            [new_coordinate_1],
            [new_coordinate_2],
            [new_coordinate_3],
            [new_coordinate_4]
        ])

        rect = cv2.minAreaRect(new_coordinate_array)
        new_box = cv2.boxPoints(rect)
        new_box = np.int0(new_box)

        # get width and height of the detected rectangle
        new_width = int(rect[1][0])
        new_height = int(rect[1][1])
        new_box_float = new_box.astype("float32")

        # coordinate of the points in box points after the rectangle has been straightened
        straightened_array = np.array([[0, new_height-1],
                            [0, 0],
                            [new_width-1, 0],
                            [new_width-1, new_height-1]], dtype="float32")

        # the perspective transformation matrix
        M = cv2.getPerspectiveTransform(new_box_float, straightened_array)

        # directly warp the rotated rectangle to get the straightened rectangle
        warped = cv2.warpPerspective(image.copy(), M, (new_width, new_height))

        (warped_H,warped_W) = warped.shape[:2]    
        if warped_H > warped_W: 
            warped = cv2.rotate(warped, cv2.ROTATE_90_CLOCKWISE)

        warped = imutils.resize(warped, width=600)
        warped = cv2.bitwise_not(warped)

        (warped_H,warped_W) = warped.shape[:2]
        warped = warped[5 : warped_H - 5, 5: warped_W-5]

        cv2.imwrite(str(image_path[image_counter]) + "/"+str(image_names[image_counter])+"_RECT.jpg", warped)
        cv2.waitKey(0)
    except:
        print("ERROR")

    # END OF CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #