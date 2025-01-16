# pip install tk

import tkinter as tk
from tkinter import *
import random

# Initialize the window
win = tk.Tk()
win.geometry("750x750")
win.title("PythonGeeks")

# Initialize variables
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()

# Set initial values
hint.set("Guess a number between 1 to 50")
score.set(5)
final_score.set(score.get())

# Random number to guess
num = random.randint(1, 50)  # Fixed missing comma

# Define the function
def fun():
    x = guess.get()
    final_score.set(score.get())
    if score.get() > 0:
        if x > 50 or x < 1:
            hint.set("Out of range! You just lost 1 chance.")
            score.set(score.get() - 1)
            final_score.set(score.get())
        elif num == x:
            hint.set("Congratulations, YOU WON!!!")
            score.set(score.get() - 1)
            final_score.set(score.get())
        elif num > x:
            hint.set("Your guess was too low: Guess a higher number.")
            score.set(score.get() - 1)
            final_score.set(score.get())
        elif num < x:
            hint.set("Your guess was too high: Guess a lower number.")
            score.set(score.get() - 1)
            final_score.set(score.get())
    else:
        hint.set("Game Over You Lost")

# Widgets
Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)
Entry(win, text=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

Label(win, text='I challenge you to guess the number ', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
Label(win, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()