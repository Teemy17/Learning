from tkinter import *
from tkinter import messagebox

#Q1
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
#------------------------------------------------------------------------------------------------------------------------------------
#Q2
import os
from tkinter import *
from tkinter import filedialog, messagebox
import pygame.mixer as mixer
from PIL import ImageTk,Image



# The layout is subject to be added or changed. This is just only the overview of the GUI.
# The image does not appear cuz I can only send .py file. Please look in the pdf file.
class App:
    def __init__(self, root):
        self.window = root
        mixer.init()
        self.main_window()
        self.option_menu()
        self.directory_list = []


       

    def main_window(self):
        Label(self.window,text="Music Player", font=("Arial",20,"bold","italic")).place(x=320,y=20)
        
        frame = Frame(self.window)
        frame.place(x = 30, y = 70)
        v_scroll = Scrollbar(frame)
        v_scroll.pack(side=RIGHT, fill=Y)

        self.song_list = Listbox(frame, bg="#404040", fg="#ffbf50", width=120, height=12, font=("Arial",8,"bold"), relief=SUNKEN, borderwidth=2, yscrollcommand=v_scroll.set)    
        self.song_list.pack(side=LEFT)
        v_scroll.configure(command=self.song_list.yview)


    def option_menu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        options_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=options_menu)
        options_menu.add_command(label="Add songs", command = self.add_song)
        

    def add_song(self):
        songs = filedialog.askopenfilenames(title="Select one or multiple song",filetypes=(("MP3 files", "*mp3"), ("WAV files","*.wav")))
        for song in songs:
            song_name = os.path.basename(song)
            directory_path = song.replace(song_name,"")
            self.directory_list.append({'path':directory_path,'song':song_name})
            self.song_list.insert(END, song_name)
        self.song_list.select_set('0')


if __name__ == "__main__":
    window = Tk()
    window.title("App")
    window.geometry("800x500")
    window.resizable(0,0)
    
    btPlay_img_get = ImageTk.PhotoImage(Image.open("Python project/Images/play.png").resize((80,80),Image.Resampling.LANCZOS))
    btPlay_img = Button(window,image= btPlay_img_get, highlightthickness = 0, bd = 0)
    btPlay_img.place(x = 250, y = 250)
    
    btPause_img_get = ImageTk.PhotoImage(Image.open("Python project/Images/pause.png").resize((80,80),Image.Resampling.LANCZOS))
    btPause_img = Button(window,image= btPause_img_get, highlightthickness = 0, bd = 0)
    btPause_img.place(x = 350, y = 250)
    
    btStop_img_get = ImageTk.PhotoImage(Image.open("Python project/Images/stop.png").resize((80,80),Image.Resampling.LANCZOS))
    btStop_img = Button(window,image= btStop_img_get, highlightthickness = 0, bd = 0)
    btStop_img.place(x = 450, y = 250)

    btNext_img_get = ImageTk.PhotoImage(Image.open("Python project/Images/next.png").resize((80,80),Image.Resampling.LANCZOS))
    btNext_img = Button(window,image= btNext_img_get, highlightthickness = 0, bd = 0)
    btNext_img.place(x = 550, y = 250)

    btPrev_img_get = ImageTk.PhotoImage(Image.open("Python project/Images/prev.png").resize((80,80),Image.Resampling.LANCZOS))
    btPrev_img = Button(window,image= btPrev_img_get, highlightthickness = 0, bd = 0)
    btPrev_img.place(x = 150, y = 250)
    
    App(window)
    window.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------
#Q3
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
        self.canvas.create_oval(x , y, x + 25, y + 25)
       

    def delete(self, event):
        closet_circle = self.canvas.find_closest(event.x, event.y)
        if closet_circle:
            self.canvas.delete(closet_circle)

Drawcircle()

    
