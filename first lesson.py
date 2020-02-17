import random
import cv2 as cv
import numpy as np
import math
import time
from matplotlib.pyplot import *

size = int(input("Enter the size of image:\n"))
image = np.zeros((size, size, 3), dtype="uint8")
lines = [((random.uniform(0, size - 1), random.uniform(0, size - 1)),
          (random.uniform(0, size - 1), random.uniform(0, size - 1)))
         for i in range(100)]
image.fill(255)
cv.imshow("image", image)


# TODO: choosing whether to show or save or both
# TODO: comment everything or migrate to the anaconda

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
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)
    if dy > dx:
        dx, dy = dy, dx
        change = True
    else:
        change = False
    epsilon = 2 * dy - dx
    for i in range(int(dx)):
        image[math.ceil(x), math.ceil(y)] = [0, 0, 0]  # drawing a black point
        while epsilon >= 0:
            if change == 1:
                x += s1
            else:
                y += s2
            epsilon -= 2 * dx
        if change == 1:
            y += s2
        else:
            x += s1
        epsilon += 2 * dy
    return image


def check(func, window_title):
    times = []
    for line in lines:
        start = time.time()

        start_point, end_point = line
        x_1, y_1 = start_point
        x_2, y_2 = end_point
        cv.imshow("white", func(x_1, y_1, x_2, y_2))
        # cv.waitKey(0)

        end = time.time()
        times.append(end - start)

    plot(times)
    title(window_title)
    show()
    return sum(times)


print(check(line_brezenham, "Brezenham"))
print(check(line_dda, "DDA"))

