import random
from tkinter import *

def roll(event = 0):
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]#[1,2,3,4,5,6]

    label1.config(text = f'{random.choice(number)} {random.choice(number)}')
    label1.pack()

win = Tk()
win.geometry("700x450")

label1 = Label(win, font=("times",200))

button = Button(win, text = "Click to roll the dice", command= roll)
button.pack()
label2= Label(win, text="Or press the enter key", font=("times",20)).pack()
win.bind('<Return>',roll)
win.mainloop()
