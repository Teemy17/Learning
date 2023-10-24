from tkinter import *

class Spinner:
    def __init__(self):
        window = Tk()
        window.title("Spinner")
        self.num = 0
        self.text = Label(window, text = self.num)
        buttonUp = Button(window, text = "+", command = self.UP)
        buttonDown = Button(window, text = "-", command = self.Down)
        buttonReset = Button(window, text = "Reset", command = self.Reset)
        buttonUp.pack()
        buttonDown.pack()
        buttonReset.pack()
        self.text.pack()
        window.mainloop()

    def UP(self):
        self.num += 1
        self.text.config(text = self.num)

    def Down(self):
        self.num -= 1
        self.text.config(text = self.num)
       
    def Reset(self):
        self.num = 0
        self.text.config(text = self.num)


Spinner()