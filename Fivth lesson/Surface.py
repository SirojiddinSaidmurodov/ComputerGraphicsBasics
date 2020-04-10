from tkinter import *

#  initializing rectangle vertex and moving, rotating coefficients
surface = [
    [0, 0, 0, 1],
    [300, 0, 0, 1],
    [300, 500, 0, 1],
    [0, 500, 0, 1]
]
#  x, y, z, xr, yr, zr
components = [0, 0, 0, 0, 0, 0]


def change(component, increase):
    global components
    delta = -5
    if increase:
        delta = 5
    components[component] += delta


root = Tk()
root.title("Геометрические преобразования прямоугольника")
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
