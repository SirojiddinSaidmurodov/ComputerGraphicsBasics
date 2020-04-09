import cv2 as cv
import numpy as np


def bezier(t, vertex):
    basis = np.array([
        [-1, 3, -3, 1],
        [3, -6, 3, 0],
        [-3, 3, 0, 0],
        [1, 0, 0, 0]
    ])
    return np.array([t ** 3, t ** 2, t, 1]) @ basis @ vertex


image = np.zeros((500, 500, 3), dtype='uint8')
image.fill(255)
points = np.array([
    [60, 300],
    [0, 50],
    [300, 50],
    [500, 300]
])

for i in range(3):
    cv.line(image, (points[i][0], points[i][1]), (points[i + 1][0], points[i + 1][1]), (150, 150, 150))

for i in np.arange(0, 1, .0001):
    point = bezier(i, points)
    image[int(point[1]), int(point[0])] = [0, 0, 255]
cv.imshow("im", image)
cv.waitKey(0)
