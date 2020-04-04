import ThirdLesson.sphere as sp
import cv2
import numpy as np
from matplotlib.pyplot import *

sphere = sp.Sphere(sp.Point3D(250, 250, 0), 200, sp.Point3D(10, 10, 10))
lines = sphere.get_points(30, 30)
print(len(lines))
image = np.zeros((500, 500, 3), dtype="uint8")
image.fill(255)
for line in lines:
    a, b = line
    cv2.line(image, (int(a.x)+250, int(a.z)+250), (int(b.x)+250, int(b.z)+250), (0, 0, 0))

cv2.imshow("im", image)
cv2.waitKey(0)
show()
