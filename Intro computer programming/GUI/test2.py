from tkinter import *
# def processOK():
#     print("Ok button is clicked")

# def processCancel():
#     print("cancel button is clicked")

# window = Tk()
# btOK = Button(window, text = "OK", fg = "red", command = processOK)
# btCancel = Button(window, text = "cancel", bg = "yellow", command = processCancel)
# btOK.pack()
# btCancel.pack()
# window.mainloop()

# Another version using class
class ButtonEventProcess:
    def __init__(self):
        window = Tk()
        btOK = Button(window, text = "OK", fg = "red", command = self.OK)
        btCancel = Button(window, text = "Cancel", bg = "yellow", command = self.Cancel)
        btOK.pack()
        btCancel.pack()
        window.mainloop()
    
    def OK(self):
        print("OK button is clicked")

    def Cancel(self):
        print("Cancel button is clicked")

ButtonEventProcess()

