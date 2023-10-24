from tkinter import *
from tkinter import messagebox
import random

class DrawCircle:
    def __init__(self):
        window = Tk()
        window.title("Bruh")
        self.canvas = Canvas(window, width = 400, height = 250, bg = "white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.circle)
        self.rectangle()
        window.mainloop()

    def rectangle(self):
        self.canvas.create_rectangle(50, 50, 350, 200, outline = "black")

    def circle(self, event):
        color = ["yellow", "black", "red", "green", "brown", "blue", "white", "brown", "pink", "purple"]
        x, y = event.x, event.y
        if 50 <= x <= 350 and 50 <= y <= 200:
            self.canvas.create_oval(x, y, x+10, y+10, fill = random.choice(color))
        else:
            messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")


DrawCircle()