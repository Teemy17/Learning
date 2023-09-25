from tkinter import *

class Drawcircle:
    def __init__(self):
        window = Tk()
        window.title("Circle bruh")
        self.canvas = Canvas(window, width= 400, height= 250, bg = "white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.circle)
        self.canvas.bind("<Button-3>", self.delete)
        window.mainloop()

    def circle(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x  - 10 , y - 10, x + 10, y + 10)
       

    def delete(self, event):
        closet_circle = self.canvas.find_closest(event.x, event.y)
        if closet_circle:
            self.canvas.delete(closet_circle)

Drawcircle()

    
