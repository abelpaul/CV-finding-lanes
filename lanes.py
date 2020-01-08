import cv2
import numpy as np

# reading image into a matrix
img = cv2.imread("test_image.jpg")

# creating an image copy so that matrices are not manipulated
lane_image= np.copy(img)

# grayscale image, meaning one channel of color rather than 3 (in RGB)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

#Applying a Gaussian Blur
blur = cv2.GaussianBlur(gray, (5,5), 0)

#Computing the gradient (Calculating the derivative)
canny = cv2.Canny(blur, 50, 50)

#strongest gradients are now outlined

# showing image in a seperate window
cv2.imshow('result', canny)
cv2.waitKey(0)

