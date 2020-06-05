from random import randint
from tkinter import *

import cv2
import numpy as np
from PIL import Image
from PIL import ImageTk

# color = np.zeros((1, 1, 3), dtype='uint8')
# color[0, 0, 1] = 255

x = 40
y = 25

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
    else:
        infect_all(ill_people)
        ill_people *= 2

    pic = image
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
    pic = Image.fromarray(pic)
    pic = ImageTk.PhotoImage(pic)
    panel.configure(image=pic)
    panel.image = pic

    healthy.set("Health people: " + str(len(people)))
    ill.set("Ill people: " + str(1000 - len(people)))


root = Tk()
root.title("CoViD-19")
root.geometry("450x400")
root.resizable(0, 0)

healthy = StringVar(root)
ill = StringVar(root)
healthy.set("Health people: " + str(len(people)))
ill.set("Ill people: " + str(1000 - len(people)))

im = image
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
im = Image.fromarray(im)
im = ImageTk.PhotoImage(im)
panel = Label(image=im)
panel.image = im
panel.place(relx=0, rely=0)

btn = Button(text="Next day", command=start)
btn.place(relx=0.8, rely=0.9)
Label(text="People: 1000").place(relx=0.7, rely=0.05)
Label(textvariable=healthy).place(relx=0.7, rely=0.15)
Label(textvariable=ill).place(relx=0.7, rely=0.25)
root.mainloop()
