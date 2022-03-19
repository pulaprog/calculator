from lib2to3.pgen2.token import MINUS
from tkinter import *

def suma():
        a = int(num1.get())
        b = int(num2.get())
        ab = a + b
        lsuma.configure(text=ab)
def diff():
        a = int(num1.get())
        b = int(num2.get())
        ab = a - b
        lsuma.configure(text=ab)
def mult():
        a = int(num1.get())
        b = int(num2.get())
        ab = a * b
        lsuma.configure(text=ab)
def divi():
        a = int(num1.get())
        b = int(num2.get())
        ab = a / b
        lsuma.configure(text=ab)


Win = Tk()
Win.title("calc")
Win.geometry("200x270")

num1 = Entry(Win)
num1.pack(pady=5)

num2 = Entry(Win)
num2.pack(pady=5)

lsuma = Label(Win, text="0")
lsuma.pack(pady=5)

suma = Button(Win, text="+", command=suma, width=15)
suma.pack(pady=5)

difference = Button(Win, text="-", command=diff, width=15)
difference.pack(pady=5)

mult = Button(Win, text="*", command=mult, width=15)
mult.pack(pady=5)

dividion = Button(Win, text="/", command=divi, width=15)
dividion.pack(pady=5)

Win.mainloop()