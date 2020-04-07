import ThirdLesson.sphere as sp
import cv2
import numpy as np

sphere = sp.Sphere(sp.Point3D(np.array([250, 250, 0, 1])), 200, sp.Point3D(np.array([35, 35, 15, 1])))
lines = sphere.get_points(18, 18)
image = np.zeros((500, 500, 3), dtype="uint8")
image.fill(255)
for line in lines:
    a, b, _ = line.to_tuple()
    cv2.line(image, (int(a.x) + 250, int(a.y) + 250), (int(b.x) + 250, int(b.y) + 250), (0, 0, 0))

cv2.imshow("im", image)
cv2.waitKey(0)
