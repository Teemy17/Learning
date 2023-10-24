from tkinter import *
from tkinter import messagebox
class Currency:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        self.num = StringVar()
        self.entry = Entry(window, textvariable = self.num)
        ToTHB = Button(window, text = "USD -> THB", command = self.USDToTHB)
        ToUSD = Button(window, text = "THB -> USD", command = self.THBToUSD)
        self.entry.pack()
        ToTHB.pack()
        ToUSD.pack()
        window.mainloop()

    def USDToTHB(self):
        USD = float(self.num.get())
        convertToTHB = USD * 30
        messagebox.showinfo("USD -> THB", f"{USD:.2f} USD = {convertToTHB:.2f} THB")

    def THBToUSD(self):
        THB = float(self.num.get())
        convertToUSD = THB / 30
        messagebox.showinfo("USD -> THB", f"{THB:.2f} THB = {convertToUSD:.2f} USD")

Currency()


    