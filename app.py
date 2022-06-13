import cv2
import numpy as np

# original image
# -1 loads as-is so if it will be 3 or 4 channel as the original
img = cv2.imread("picture.jpg", -1)

points = []
isClicked = False


def draw(event, x, y, flag, params):
    global isClicked
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        isClicked = True
        points.append((x, y))
    if event == cv2.EVENT_LBUTTONUP:
        isClicked = False

    if len(points) > 1 and isClicked:
        pt1 = (points[-2][0], points[-2][1])
        pt2 = (points[-1][0], points[-1][1])

        cv2.line(img, pt1, pt2, (255, 255, 255), 1)


def save_image(img):
    global points

    mask = np.zeros(img.shape, dtype=np.uint8)

    roi_corners = np.array(points)

    channel_count = img.shape[2]

    ignore_mask_color = (255,)*channel_count
    cv2.fillPoly(mask, np.array(
        [roi_corners], dtype=np.int32), ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    cv2.imwrite('cropped.png', masked_image)


cv2.namedWindow('window')
cv2.setMouseCallback("window", draw)

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
