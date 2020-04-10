import cv2 as cv

image = cv.imread("1.jpg")
for (x, y, h, w) in cv.CascadeClassifier("haarcascade_frontalface_alt_tree.xml").detectMultiScale(image):
    img = cv.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
cv.imshow("faces", image)
cv.waitKey(0)
