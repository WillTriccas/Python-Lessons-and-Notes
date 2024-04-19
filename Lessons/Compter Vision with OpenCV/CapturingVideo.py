import cv2
import time

framerate_counter = 0
video = cv2.VideoCapture(0)

while True:
    framerate_counter = framerate_counter + 1

    check, frames = video.read()
    cv2.imshow("Capturing", frames)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break


print(framerate_counter)

video.release()
cv2.destroyAllWindows()