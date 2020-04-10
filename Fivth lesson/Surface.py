import math
from tkinter import *

import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageTk

#  initializing rectangle vertex and moving, rotating coefficients
rectangle_vertex = [
    [50, 50, 0, 1],
    [200, 50, 0, 1],
    [200, 300, 0, 1],
    [50, 300, 0, 1]
]
#  x, y, z, xr, yr, zr
components_values = [0, 0, 0, 0, 0, 0]
panel = None


def change(component, increase):
    global components_values, panel, rectangle_vertex
    delta = -5
    if increase:
        delta = 5
    components_values[component] += delta

    im = rectangle_drawer(np.array(rectangle_vertex), components_values)
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


def rectangle_drawer(rectangle, components):
    image = np.zeros((500, 800, 3), dtype='uint8')
    rx = math.radians(components[3])
    ry = math.radians(components[4])
    rz = math.radians(components[5])
    Rx = np.array([[1, 0, 0, 0],
                   [0, math.cos(rx), math.sin(rx), 0],
                   [0, -math.sin(rx), math.cos(rx), 0],
                   [0, 0, 0, 1]])
    Ry = np.array([[math.cos(ry), 0, -math.sin(ry), 0],
                   [0, 1, 0, 0],
                   [math.sin(ry), 0, math.cos(ry), 0],
                   [0, 0, 0, 1]])
    Rz = np.array([[math.cos(rz), math.sin(rz), 0, 0],
                   [-math.sin(rz), math.cos(rz), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    rot_matrix = Rx @ Ry @ Rz
    rot_rec = rectangle @ rot_matrix
    moved_rec = rot_rec + np.array([
        [components[0], components[1], components[2], 0],
        [components[0], components[1], components[2], 0],
        [components[0], components[1], components[2], 0],
        [components[0], components[1], components[2], 0]
    ])
    pts = np.array([moved_rec[:, :2]], 'int32')
    cv.fillPoly(image, pts, color=[104, 255, 255])
    return image


root = Tk()
root.title("Геометрические преобразования прямоугольника. Автор: Саидмуродов Сирожиддин")
root.geometry("1000x500+50+50")

button_x_plus = Button(root, text="+", height=1, width=1, command=lambda c=0, i=True: change(c, i))
button_x_minus = Button(root, text="-", height=1, width=1, command=lambda c=0, i=False: change(c, i))
button_y_plus = Button(root, text="+", height=1, width=1, command=lambda c=1, i=True: change(c, i))
button_y_minus = Button(root, text="-", height=1, width=1, command=lambda c=1, i=False: change(c, i))
button_z_plus = Button(root, text="+", height=1, width=1, command=lambda c=2, i=True: change(c, i))
button_z_minus = Button(root, text="-", height=1, width=1, command=lambda c=2, i=False: change(c, i))
button_xr_plus = Button(root, text="+", height=1, width=1, command=lambda c=3, i=True: change(c, i))
button_xr_minus = Button(root, text="-", height=1, width=1, command=lambda c=3, i=False: change(c, i))
button_yr_plus = Button(root, text="+", height=1, width=1, command=lambda c=4, i=True: change(c, i))
button_yr_minus = Button(root, text="-", height=1, width=1, command=lambda c=4, i=False: change(c, i))
button_zr_plus = Button(root, text="+", height=1, width=1, command=lambda c=5, i=True: change(c, i))
button_zr_minus = Button(root, text="-", height=1, width=1, command=lambda c=5, i=False: change(c, i))

button_x_plus.place(relx=.85, rely=.00)
button_x_minus.place(relx=.85, rely=.05)
Label(text="Сдвиг по оси X").place(relx=.87, rely=.025)

button_y_plus.place(relx=.85, rely=.11)
button_y_minus.place(relx=.85, rely=.16)
Label(text="Сдвиг по оси Y").place(relx=.87, rely=.135)

button_z_plus.place(relx=.85, rely=.22)
button_z_minus.place(relx=.85, rely=.27)
Label(text="Сдвиг по оси Z").place(relx=.87, rely=.245)

button_xr_plus.place(relx=.85, rely=.33)
button_xr_minus.place(relx=.85, rely=.38)
Label(text="Угол по оси X").place(relx=.87, rely=.355)

button_yr_plus.place(relx=.85, rely=.44)
button_yr_minus.place(relx=.85, rely=.49)
Label(text="Угол по оси Y").place(relx=.87, rely=.465)

button_zr_plus.place(relx=.85, rely=.55)
button_zr_minus.place(relx=.85, rely=.60)
Label(text="Угол по оси Z").place(relx=.87, rely=.575)

root.mainloop()
