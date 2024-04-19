import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    resized_images = cv2.resize(img,(100,100))
    cv2.imshow("Hey", resized_images)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


    cv2.imwrite("resized_" + image, resized_images)
