import os
from tkinter import *
from tkinter import filedialog, messagebox
import pygame.mixer as mixer
from PIL import ImageTk, Image
import time
import threading
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, APIC
import io


class BaseButton:
    def __init__(self, root, app, image_path, x, y):
        self.app = app
        self.button = Button(root, highlightthickness=0, bd=0)
        self.button_img = ImageTk.PhotoImage(
            Image.open(image_path).resize((80, 80), Image.LANCZOS)
        )
        self.button.config(image=self.button_img, command=self.action)
        self.button.place(x=x, y=y)

    def action(self):
        pass


class PlayButton(BaseButton):
    def action(self):
        if self.app.song_list.curselection():
            song_info = self.app.directory_list[self.app.song_list.curselection()[0]]
            mixer.music.load(song_info["path"] + song_info["song"])
            mixer.music.play()

            self.app.current_song_index = self.app.song_list.curselection()[0]
            song_type = MP3(song_info["path"] + song_info["song"])
            self.app.song_length = song_type.info.length

            album_art = self.get_album_art(song_info["path"] + song_info["song"])
            self.app.display_album_art(album_art)

            SongDuration(self.app).song_duration_time()
        else:
            messagebox.showerror("Error", "Please select a song to play")

    def get_album_art(self, song_path):
        audio = MP3(song_path, ID3=ID3)
        album_art = None
        for tag in audio.tags.values():
            if tag.FrameID.startswith("APIC"):  # Check for any APIC frame
                if tag.mime.startswith("image/jpeg"):  # Check for JPEG image
                    album_art = tag
                break
        if album_art:
            return album_art
        else:
            return None


class PauseButton(BaseButton):
    def action(self):
        if self.app.paused == False:
            self.app.paused = True
            mixer.music.pause()
            SongDuration(self.app).song_duration_time()
        else:
            self.app.paused = False
            mixer.music.unpause()
            SongDuration(self.app).song_duration_time()


class StopButton(BaseButton):
    def action(self):
        mixer.music.stop()
        self.app.song_list.select_clear(0, END)
        self.app.paused = False
        SongDuration(self.app)


class NextButton(BaseButton):
    def action(self):
        if self.app.current_song_index + 1 < len(self.app.directory_list):
            next_song_index = self.app.current_song_index + 1
            song_info = self.app.directory_list[next_song_index]
            mixer.music.load(song_info["path"] + song_info["song"])
            mixer.music.play()
            self.app.current_song_index = next_song_index
            self.app.song_list.select_clear(0, END)
            self.app.song_list.select_set(next_song_index)
            self.app.song_list.activate(next_song_index)

            album_art = self.get_album_art(song_info["path"] + song_info["song"])
            self.app.display_album_art(album_art)

            SongDuration(self.app).song_duration_time()
        else:
            print("No more songs in the list")

    def get_album_art(self, song_path):
        audio = MP3(song_path, ID3=ID3)
        album_art = None
        for tag in audio.tags.values():
            if tag.FrameID.startswith("APIC"):  # Check for any APIC frame
                if tag.mime.startswith("image/jpeg"):  # Check for JPEG image
                    album_art = tag
                break
        if album_art:
            return album_art
        else:
            return None


class PrevButton(BaseButton):
    def action(self):
        if self.app.current_song_index > 0:
            prev_song_index = self.app.current_song_index - 1
            song_info = self.app.directory_list[prev_song_index]
            mixer.music.load(song_info["path"] + song_info["song"])
            mixer.music.play()
            self.app.current_song_index = prev_song_index
            self.app.song_list.select_clear(0, END)
            self.app.song_list.select_set(prev_song_index)
            self.app.song_list.activate(prev_song_index)

            album_art = self.get_album_art(song_info["path"] + song_info["song"])
            self.app.display_album_art(album_art)

        else:
            print("This is the first song in the list")

    def get_album_art(self, song_path):
        audio = MP3(song_path, ID3=ID3)
        album_art = None
        for tag in audio.tags.values():
            if tag.FrameID.startswith("APIC"):  # Check for any APIC frame
                if tag.mime.startswith("image/jpeg"):  # Check for JPEG image
                    album_art = tag
                break
        if album_art:
            return album_art
        else:
            return None


class DeleteButton(BaseButton):
    def action(self):
        selected_index = self.app.song_list.curselection()
        if selected_index:
            selected_song = self.app.directory_list.pop(selected_index[0])
            if selected_index[0] == self.app.current_song_index:
                mixer.music.stop()
            self.app.song_list.delete(selected_index[0])
            print(f"Deleted song: {selected_song}")
        else:
            messagebox.showerror("Error", "Please select a song to delete")


class App:
    def __init__(self, root):
        self.window = root
        mixer.init()
        self.main_window()
        self.directory_list = []
        self.option_menu()

        self.btPlay_img = PlayButton(
            self.window, self, "Python project/Images/play.png", 250, 250
        )
        self.btPause_img = PauseButton(
            self.window, self, "Python project/Images/pause.png", 350, 250
        )
        self.btStop_img = StopButton(
            self.window, self, "Python project/Images/stop.png", 450, 250
        )
        self.btNext_img = NextButton(
            self.window, self, "Python project/Images/next.png", 550, 250
        )
        self.btPrev_img = PrevButton(
            self.window, self, "Python project/Images/prev.png", 150, 250
        )
        self.btDelete_img = DeleteButton(
            self.window, self, "Python project/Images/delete.png", 700, 250
        )

        self.current_song_index = 0
        self.paused = False

        self.song_duration_bar = 0
        self.song_length = 0

        self.album_art_label = Label(self.window, bg="#141414", relief=SUNKEN)
        self.album_art_label.place(x=30, y=330, width=150, height=150)

    def main_window(self):
        Label(
            self.window, text="Music Player", font=("Arial", 20, "bold", "italic")
        ).place(x=320, y=20)

        frame = Frame(self.window)
        frame.place(x=30, y=70)
        v_scroll = Scrollbar(frame)
        v_scroll.pack(side=RIGHT, fill=Y)

        self.song_list = Listbox(
            frame,
            bg="#404040",
            fg="#ffbf50",
            width=120,
            height=12,
            font=("Arial", 8, "bold"),
            relief=SUNKEN,
            borderwidth=2,
            yscrollcommand=v_scroll.set,
        )
        self.song_list.pack(side=LEFT)
        v_scroll.configure(command=self.song_list.yview)

        self.volume_slider = Scale(
            self.window, from_=0, to=100, orient=HORIZONTAL, command=self.volume
        )
        self.volume_slider.set(50)
        self.volume_slider.place(x=650, y=400)

    def option_menu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        options_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=options_menu)
        options_menu.add_command(label="Add songs", command=self.add_song)
        options_menu.add_command(label="Add folder", command=self.add_folder)

    def add_song(self):
        songs = filedialog.askopenfilenames(
            title="Select one or multiple song",
            filetypes=(("MP3 files", "*.mp3"), ("WAV files", "*.wav")),
        )
        for song in songs:
            song_name = os.path.basename(song)
            directory_path = song.replace(song_name, "")
            self.directory_list.append({"path": directory_path, "song": song_name})
            self.song_list.insert(END, song_name)
        self.song_list.select_set("0")

    def add_folder(self):
        folder_path = filedialog.askdirectory(title="Select a folder containing songs")
        if folder_path:
            songs = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]
            if songs:
                for song in songs:
                    song_name = os.path.basename(song)
                    self.directory_list.append(
                        {"path": folder_path + "/", "song": song_name}
                    )
                    self.song_list.insert(END, song_name)
                self.song_list.select_set(0)
            else:
                messagebox.showinfo(
                    "Info", "No MP3 files found in the selected folder."
                )
        else:
            messagebox.showinfo("Info", "No folder selected.")

    def display_album_art(self, album_art):
        if album_art is not None:
            img_data = album_art.data
            img = Image.open(io.BytesIO(img_data))
            img = img.resize(
                (150, 150), Image.LANCZOS
            )  # Resize the album art as needed
            album_art_img = ImageTk.PhotoImage(img)
            self.album_art_label.config(image=album_art_img)
            self.album_art_label.image = album_art_img
        else:
            default_img_path = "Python project/Images/default.png"  
            default_img = Image.open(default_img_path)
            default_img = default_img.resize((150, 150), Image.LANCZOS)

            default_album_art_img = ImageTk.PhotoImage(default_img)
            self.album_art_label.config(image=default_album_art_img)
            self.album_art_label.image = default_album_art_img

    def volume(self, val):
        volume = int(val) / 100
        mixer.music.set_volume(volume)

    def Shuffle(self):
        pass

    def Repeat(self):
        pass


class SongDuration:
    def __init__(self, app):
        self.app = app
        self.song_duration_bar = Label(
            self.app.window,
            text="Song Duration",
            font=("Arial", 17, "bold"),
            fg="white",
            bg="#141414",
            width=25,
        )
        self.song_duration_bar.place(x=220, y=400)
        self.update_thread = None  # Initialize the update thread

    def start_update_thread(self):
        if not self.update_thread:
            self.update_thread = threading.Thread(target=self.song_duration_time)
            self.update_thread.daemon = True
            self.update_thread.start()

    def update_song_duration_label(self, current_time):
        song_info = self.app.directory_list[self.app.current_song_index]
        song_type = MP3(song_info["path"] + song_info["song"])
        song_length = song_type.info.length
        self.song_duration_bar.config(
            text=f"Time is: {self.format_time(current_time)} of {self.format_time(song_length)}"
        )

    def song_duration_time(self):
        try:
            while mixer.music.get_busy():
                current_time = mixer.music.get_pos() / 1000
                self.update_song_duration_label(current_time)
                self.app.window.update()
                time.sleep(0.1)
        except Exception as e:
            print("Error in song duration:", str(e))

    def format_time(self, time_in_seconds):
        minutes, seconds = divmod(int(time_in_seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    window = Tk()
    window.title("Music Player")
    window.geometry("800x500")
    window.resizable(0, 0)

    app = App(window)
    song_duration = SongDuration(app)
    song_duration.start_update_thread()

    window.mainloop()
