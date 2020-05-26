from tkinter import *

import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageTk

import Additional.cylinder as cy

components_values = [0, 0, 180, 1]
panel = None


def change(component, increase):
    global components_values, panel
    delta = -5
    if increase:
        delta = 5
    components_values[component] += delta
    cylinder = cy.Cylinder(np.array([250, 250, 250, 1]), 50, 200, np.array(components_values))
    lines = cylinder.get_lines(30, 10)
    image = np.zeros((500, 800, 3), dtype="uint8")
    image.fill(255)

    for i in range(len(lines)):
        a, b = lines[i]
        cv.line(image, (int(a[0]) + 250, int(a[1]) + 250), (int(b[0]) + 250, int(b[1]) + 250), (0, 0, 0))

    im = image
    im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
    im = Image.fromarray(im)
    im = ImageTk.PhotoImage(im)
    if panel is None:
        panel = Label(image=im)
        panel.pack(side="left")
    else:
        panel.configure(image=im)
        panel.image = im


root = Tk()
root.title("Геометрические преобразования прямоугольника. Автор: Саидмуродов Сирожиддин")
root.geometry("1000x500+50+50")

button_x_plus = Button(root, text="+", height=1, width=1, command=lambda c=0, i=True: change(c, i))
button_x_minus = Button(root, text="-", height=1, width=1, command=lambda c=0, i=False: change(c, i))
button_y_plus = Button(root, text="+", height=1, width=1, command=lambda c=1, i=True: change(c, i))
button_y_minus = Button(root, text="-", height=1, width=1, command=lambda c=1, i=False: change(c, i))
button_z_plus = Button(root, text="+", height=1, width=1, command=lambda c=2, i=True: change(c, i))
button_z_minus = Button(root, text="-", height=1, width=1, command=lambda c=2, i=False: change(c, i))

button_x_plus.place(relx=.85, rely=.00)
button_x_minus.place(relx=.85, rely=.05)
Label(text="поворот по оси X").place(relx=.87, rely=.025)

button_y_plus.place(relx=.85, rely=.11)
button_y_minus.place(relx=.85, rely=.16)
Label(text="поворот по оси Y").place(relx=.87, rely=.135)

button_z_plus.place(relx=.85, rely=.22)
button_z_minus.place(relx=.85, rely=.27)
Label(text="поворот по оси Z").place(relx=.87, rely=.245)

root.mainloop()
