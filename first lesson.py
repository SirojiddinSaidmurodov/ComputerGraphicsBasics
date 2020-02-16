import random
import cv2 as cv
import numpy as np
import math
import time
from matplotlib.pyplot import *

size = int(input("Enter the size of image:\n"))
image = np.zeros((size, size, 3), dtype="uint8")


def sign(number):
    result = 1 if number > 0 else -1 if number < 0 else 0
    return result


def line_dda(x1, y1, x2, y2):
    image.fill(255)
    if abs(x2 - x1) >= abs(y2 - y1):
        length = abs(x2 - x1)
    else:
        length = abs(y2 - y1)
    dx = (x2 - x1) / length
    dy = (y2 - y1) / length
    x = x1 + 0.5 * sign(dx)
    y = y1 + 0.5 * sign(dy)
    for i in range(int(length)):
        image[math.ceil(x), math.ceil(y)] = [0, 0, 0]  # drawing a black point
        x += dx
        y += dy
    return image


def line_brezenham(x1, y1, x2, y2):
    image.fill(255)
    return image


lines = [((random.uniform(0, size), random.uniform(0, size)), (random.uniform(0, size), random.uniform(0, size))) for i
         in range(100)]
times = []
for line in lines:
    start = time.time()

    start_point, end_point = line
    x_1, y_1 = start_point
    x_2, y_2 = end_point
    # cv.imshow("white", dda_line(x_1, y_1, x_2, y_2))
    line_dda(x_1, y_1, x_2, y_2)

    end = time.time()
    times.append(end - start)

plot(times)
show()
print(sum(times))
