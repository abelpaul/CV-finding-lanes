import cv2
import numpy as np

# grayscale image, meaning one channel of color rather than 3 (in RGB)
#Applying a Gaussian Blur
#Computing the gradient (Calculating the derivative)
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 50)
    return canny

# reading image into a matrix
img = cv2.imread("test_image.jpg")

# creating an image copy so that matrices are not manipulated
lane_image= np.copy(img)

canny = canny(lane_image)
#strongest gradients are now outlined

# showing image in a seperate window
cv2.imshow('result', canny)
cv2.waitKey(0)

