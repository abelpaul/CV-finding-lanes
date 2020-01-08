import cv2
import numpy as np

# reading image into a matrix
img = cv2.imread("test_image.jpg")

# creating an image copy so that matrices are not manipulated
lane_image= np.copy(img)

# grayscale iamge
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

# showing image in a seperate window
cv2.imshow('result', gray)
cv2.waitKey(0)

