import cv2

img = cv2.imread("galaxy.jpg", 0)

 # print(img)

# cv2.imshow("Galaxy",img)
# cv2.waitKey(5000)
# cv2.destroyAllWindows() 

# in the resize image arguments, it is width followed by height 

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imwrite("Galaxy_Resized.jpg", resized_image)

cv2.imshow("Galaxy_Resized", resized_image)
cv2.waitKey()
cv2.destroyAllWindows()

