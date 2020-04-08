import ThirdLesson.sphere as sp
import cv2
import numpy as np

sphere = sp.Sphere(np.array([250, 250, 250, 1]), 200, np.array([60, 30, 10, 1]))
lines = sphere.get_lines(30, 30)
image = np.zeros((500, 500, 3), dtype="uint8")
image.fill(255)

for i in range(len(lines)):
    a, b = lines[i]
    cv2.line(image, (int(a[0]) + 250, int(a[1]) + 250), (int(b[0]) + 250, int(b[1]) + 250), (0, 0, 0))

cv2.imshow("im", image)
cv2.waitKey(0)
