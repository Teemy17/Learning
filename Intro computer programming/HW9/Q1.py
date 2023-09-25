from tkinter import *
from tkinter import messagebox

class Phone:
    def __init__(self):
        window = Tk()
        window.title("KMITL Phone")
        window.resizable(0,0)
        
        self.textbox = Entry(window, justify= "right", font=("Arial", 16))
        self.textbox.grid(row = 1, padx = 8, pady = 8)

        self.Button1 = Button(window, width = 5, text = "1", font= ("Arial", 16), command= lambda: self.UpdateValue(1))
        self.Button1.grid(row = 2, sticky= "W")

        self.Button2 = Button(window, width = 5, text = "2", font = ("Arial", 16), command= lambda: self.UpdateValue(2))
        self.Button2.grid(row = 2)

        self.Button3 = Button(window, width = 5, text = "3", font = ("Arial", 16), command= lambda: self.UpdateValue(3))
        self.Button3.grid(row = 2, sticky= "E")

        self.Button4 = Button(window, width = 5, text = "4", font = ("Arial", 16), command= lambda: self.UpdateValue(4))
        self.Button4.grid(row = 3, sticky= "W")

        self.Button5 = Button(window, width = 5, text = "5", font = ("Arial", 16), command= lambda: self.UpdateValue(5))
        self.Button5.grid(row = 3)

        self.Button6 = Button(window, width = 5, text = "6", font = ("Arial", 16), command= lambda: self.UpdateValue(6))
        self.Button6.grid(row = 3, sticky= "E")

        self.Button7 = Button(window, width = 5, text = "7", font = ("Arial", 16), command= lambda: self.UpdateValue(7))
        self.Button7.grid(row = 4, sticky= "W")

        self.Button8 = Button(window, width = 5, text = "8", font = ("Arial", 16), command= lambda: self.UpdateValue(8))
        self.Button8.grid(row = 4)

        self.Button9 = Button(window, width = 5, text = "9", font = ("Arial", 16), command= lambda: self.UpdateValue(9))
        self.Button9.grid(row = 4, sticky= "E")

        self.ButtonAsterisk = Button(window, width = 5, text = "*", font = ("Arial", 16), command= lambda: self.UpdateValue("#"))
        self.ButtonAsterisk.grid(row = 5, sticky= "W")

        self.Button0 = Button(window, width = 5, text = "0", font = ("Arial", 16), command= lambda: self.UpdateValue(0))
        self.Button0.grid(row = 5)

        self.ButtonHash = Button(window, width = 5, text = "#", font = ("Arial", 16), command= lambda: self.UpdateValue("#"))
        self.ButtonHash.grid(row = 5, sticky= "E")

        self.ButtonTalk = Button(window, width = 8, text = "Talk", font = ("Arial", 16), command= self.Talk)
        self.ButtonTalk.grid(row = 6, sticky= "W")

        self.ButtonDel = Button(window, width = 8, text = "<", font = ("Arial", 16), command= self.Del)
        self.ButtonDel.grid(row = 6, sticky= "E")
        
        window.mainloop()

    def UpdateValue(self, char):
        self.textbox.insert(END, char)

    def Del(self):
        self.textbox.delete(len(self.textbox.get()) - 1, END)

    def Talk(self):
        messagebox.showinfo("Dial", f"Dialling <<{self.textbox.get()}>>")


Phone()