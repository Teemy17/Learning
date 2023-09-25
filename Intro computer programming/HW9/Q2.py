import os
from tkinter import *
from tkinter import filedialog, messagebox
import pygame.mixer as mixer
from PIL import ImageTk,Image



# The layout is subject to be added or changed. This is just only the overview of the GUI.
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
    
    