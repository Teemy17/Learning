from tkinter import *

class Widgets:
    def __init__(self):
        window = Tk()
        window.title("Widgets")

        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "bold",variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text= "bold", bg = "red")
        
