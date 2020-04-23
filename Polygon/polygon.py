import math
from tkinter import *

import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageTk

#  initializing rectangle vertex and moving, rotating coefficients
polygon_vertex = [
    [100, 100],
    [200, 100],
    [250, 200],
    [250, 300],
    [100, 250]
]
polygon_center = [200, 200]
#  scale_x, scale_y, angle
components_values = [1, 1, 0]
panel = None


def change(component, increase):
    global components_values, panel, polygon_vertex, polygon_center
    if component == 2:
        delta = -5
        if increase:
            delta = 5
    if component < 2:
        delta = -0.1
        if increase:
            delta = .1
    components_values[component] += delta

    im = polygon_drawer(polygon_vertex, polygon_center, components_values)
    im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
    im = Image.fromarray(im)
    im = ImageTk.PhotoImage(im)
    if panel is None:
        panel = Label(image=im)
        panel.image = im
        panel.pack(side="left")
    else:
        panel.configure(image=im)
        panel.image = im


def draw(points, center, image, color):
    cv.fillPoly(image, np.int32([points]), color=[255, 255, 255])
    # cv.polylines(image, np.int32([points]), isClosed=True, color=[255, 255, 255], thickness=1)
    # image[center[0], center[1], :] = 255
    # stack = [(center[0], center[1])]
    # while len(stack) > 0:
    #     pixel_x, pixel_y = stack.pop()
    #     pixel_x, pixel_y = int(pixel_x), int(pixel_y)
    #     if np.any(image[pixel_x, pixel_y] == 0):
    #         image[pixel_x, pixel_y] = color
    #
    #     if np.any(image[pixel_x + 1, pixel_y] == 0):
    #         stack.append((pixel_x + 1, pixel_y))
    #     if np.any(image[pixel_x, pixel_y + 1] == 0):
    #         stack.append((pixel_x, pixel_y + 1))
    #     if np.any(image[pixel_x - 1, pixel_y] == 0):
    #         stack.append((pixel_x - 1, pixel_y))
    #     if np.any(image[pixel_x, pixel_y - 1] == 0):
    #         stack.append((pixel_x, pixel_y - 1))
    return image


def polygon_drawer(polygon, center, components):
    image = np.zeros((500, 800, 3), dtype='uint8')
    rx = math.radians(components[2])
    x = components[0]
    y = components[1]
    pts = np.dot(np.dot(np.array(polygon), np.array([[x, 0], [0, y]])), np.array(
        [[math.cos(rx), math.sin(rx)], [-math.sin(rx), math.cos(rx)]]))
    center_pt = np.dot(np.dot(np.array(center), np.array([[x, 0], [0, y]])), np.array(
        [[math.cos(rx), math.sin(rx)], [-math.sin(rx), math.cos(rx)]]))
    return draw(pts, center_pt, image, (255, 255, 255))


root = Tk()
root.title("Геометрические преобразования многоугольника")
root.geometry("1000x505+50+50")

scale_x_plus = Button(root, text="+", height=1, width=1, command=lambda c=0, i=True: change(c, i))
scale_x_minus = Button(root, text="-", height=1, width=1, command=lambda c=0, i=False: change(c, i))
scale_y_plus = Button(root, text="+", height=1, width=1, command=lambda c=1, i=True: change(c, i))
scale_y_minus = Button(root, text="-", height=1, width=1, command=lambda c=1, i=False: change(c, i))
angle_plus = Button(root, text="+", height=1, width=1, command=lambda c=2, i=True: change(c, i))
angle_minus = Button(root, text="-", height=1, width=1, command=lambda c=2, i=False: change(c, i))

scale_x_plus.place(relx=.85, rely=.00)
scale_x_minus.place(relx=.85, rely=.05)
Label(text="Масштаб по X").place(relx=.87, rely=.025)

scale_y_plus.place(relx=.85, rely=.11)
scale_y_minus.place(relx=.85, rely=.16)
Label(text="Масштаб по оси Y").place(relx=.87, rely=.135)

angle_plus.place(relx=.85, rely=.33)
angle_minus.place(relx=.85, rely=.38)
Label(text="Угол поворота").place(relx=.87, rely=.355)

root.mainloop()
