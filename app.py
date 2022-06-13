import cv2
import numpy as np

# original image
# -1 loads as-is so if it will be 3 or 4 channel as the original
img = cv2.imread("picture.jpg", -1)

def save_image(img):
    pass

while True:

    cv2.imshow("window", img)

    # read keyboard input
    key = cv2.waitKey(1)

    # when drawing is over, press 's' to save cropped image.
    if key == ord("s"):
        save_image(img)

    # break the loop and quit.
    if key & 0xFF == ord('q'):
        break
