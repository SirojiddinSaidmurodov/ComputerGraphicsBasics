import ThirdLesson.sphere as sp
import cv2
import numpy as np
from matplotlib.pyplot import *

sphere = sp.Sphere(sp.Point3D(250, 250, 0), 200)
lines = sphere.get_points(30, 30)
print(len(lines))
image = np.zeros((500, 500, 3), dtype="uint8")
for line in lines:
    a, b = line
    print(str(a) + " : " + str(b))
    cv2.line(image, (int(a.x), int(a.y)), (int(b.x), int(b.y)), (255, 255, 255))

cv2.imshow("im", image)
cv2.waitKey(0)
show()
