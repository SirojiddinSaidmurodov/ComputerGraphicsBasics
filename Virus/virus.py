from random import randint
from tkinter import *

import cv2
import numpy as np
from PIL import Image
from PIL import ImageTk

# color = np.zeros((1, 1, 3), dtype='uint8')
# color[0, 0, 1] = 255

x = 60
y = 100

ill_people = 0
people = []
for a in range(x):
    for b in range(y):
        people.append((a, b))

image = np.zeros((10 * x, 10 * y, 3), dtype='uint8')


def infect():
    temp_x, temp_y = people.pop(randint(0, len(people) - 1))
    color = np.zeros((1, 1, 3), dtype='uint8')
    color[0, 0, 0] = randint(0, 255)
    color[0, 0, 1] = randint(0, 255)
    color[0, 0, 2] = randint(0, 255)
    image[temp_x * 10:(temp_x + 1) * 10, temp_y * 10:(temp_y + 1) * 10] = color


def infect_all(people_count):
    while people_count != 0 and len(people) != 0:
        people_count -= 1
        infect()


def start():
    global ill_people
    if ill_people <= 0 or ill_people >= (x * y):
        ill_people = 1
        infect()
    infect_all(ill_people)
    ill_people *= 2

    pic = image
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
    pic = Image.fromarray(pic)
    pic = ImageTk.PhotoImage(pic)
    panel.configure(image=pic)
    panel.image = pic


root = Tk()
root.title("CoViD-19")

im = image
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
im = Image.fromarray(im)
im = ImageTk.PhotoImage(im)
panel = Label(image=im)
panel.image = im
panel.pack(side='top')

btn = Button(text="update", command=start)
btn.pack(side="bottom")
root.mainloop()
