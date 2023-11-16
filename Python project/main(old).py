import os
from tkinter import *
from tkinter import filedialog, messagebox
import pygame.mixer as mixer
from PIL import ImageTk,Image


class App:
    def __init__(self, root, btPlay_img, btPause_img, btStop_img, btNext_img, btPrev_img):
        self.window = root
        mixer.init()
        self.main_window()
        self.directory_list = []
        self.option_menu()

        self.btPlay_img = btPlay_img
        self.btPause_img = btPause_img
        self.btStop_img = btStop_img
        self.btNext_img = btNext_img
        self.btPrev_img = btPrev_img

        self.btPlay_img.config(command=self.Play)
        self.btPause_img.config(command=self.Pause)
        self.btStop_img.config(command=self.Stop)
        self.btNext_img.config(command=self.Next)
        self.btPrev_img.config(command=self.Previous)

        self.current_song_index = 0
        self.paused = False

    def main_window(self):
        Label(self.window,text="Music Player", font=("Arial",20,"bold","italic")).place(x=320,y=20)
        
        frame = Frame(self.window)  
        frame.place(x = 30, y = 70)
        v_scroll = Scrollbar(frame)
        v_scroll.pack(side=RIGHT, fill=Y)

        self.song_list = Listbox(frame, bg="#404040", fg="#ffbf50", width=120, height=12, font=("Arial",8,"bold"), relief=SUNKEN, borderwidth=2, yscrollcommand=v_scroll.set)    
        self.song_list.pack(side=LEFT)
        v_scroll.configure(command=self.song_list.yview)

        self.volume_slider = Scale(self.window, from_=0, to=100, orient=HORIZONTAL, command=self.volume)
        self.volume_slider.set(50)
        self.volume_slider.place(x=650, y=400)


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

    def Play(self):
        if self.song_list.curselection():
            song_info = self.directory_list[self.song_list.curselection()[0]]
            mixer.music.load(song_info['path'] + song_info['song'])
            mixer.music.play()
            self.current_song_index = self.song_list.curselection()[0]
        else:
            messagebox.showerror("Error", "Please select a song to play")

                
    def Pause(self):
        if self.paused == False:
            self.paused = True
            mixer.music.pause()
        else:
            self.paused = False
            mixer.music.unpause()

    def Stop(self):
        mixer.music.stop()
        self.song_list.select_clear(0,END)
        self.paused = False

    
    def Next(self):
        if self.current_song_index + 1 < len(self.directory_list):
            next_song_index = self.current_song_index + 1
            song_info = self.directory_list[next_song_index]
            mixer.music.load(song_info['path'] + song_info['song'])
            mixer.music.play()
            self.current_song_index = next_song_index
            self.song_list.select_clear(0, END)
            self.song_list.select_set(next_song_index)
            self.song_list.activate(next_song_index)
        else:
            # Handle when it's the last song in the list
            print("No more songs in the list")

    def Previous(self):
        if self.current_song_index > 0:
            prev_song_index = self.current_song_index - 1
            song_info = self.directory_list[prev_song_index]
            mixer.music.load(song_info['path'] + song_info['song'])
            mixer.music.play()
            self.current_song_index = prev_song_index
            self.song_list.select_clear(0, END)
            self.song_list.select_set(prev_song_index)
            self.song_list.activate(prev_song_index)
        else:
            # Handle when it's the first song in the list
            print("This is the first song in the list")

    def volume(self, val):
        volume = int(val)/100
        mixer.music.set_volume(volume)

    def duration_bar(self):
        pass

    
    def Repeat(self):
        pass


if __name__ == "__main__":
    window = Tk()
    window.title("Music Player")
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

    # btAutoplay_img_get = ImageTk.PhotoImage(Image.open("Python project/Images/autoplay.png").resize((80,80),Image.Resampling.LANCZOS))
    # btAutoplay_img = Button(window,image= btAutoplay_img_get, highlightthickness = 0, bd = 0)
    # btAutoplay_img.place(x = 350, y = 350)

    
    


    app = App(window, btPlay_img, btPause_img, btStop_img, btNext_img, btPrev_img)
    


   
    window.mainloop()
    
    