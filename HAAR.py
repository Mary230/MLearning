from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle
photo = imread('photo_2.jpg')
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
frame = classifier.detectMultiScale(photo)
for box in frame:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    rectangle(photo, (x, y), (x2, y2), (225, 89, 255), 1)
imshow('itsme', photo)
waitKey(0)
destroyAllWindows()
