from tkinter import *
class CanvasDrawing:
    def __init__(self):
        window = Tk()
        window.title("A simple paint program")
        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()
        self.pencolor = "black"
        self.lines = []
        self.drawing = False
        self.last_x, self.last_y = None, None
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        ResetButton = Button(window, text = "Reset", command = self.reset)
        ResetButton.pack()
        window.mainloop()

    def start_draw(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            line = self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pencolor, width=2)
            self.lines.append(line)  
            self.last_x, self.last_y = x, y

    def stop_draw(self):
        self.drawing = False

    def reset(self):
        self.canvas.delete("all")

CanvasDrawing()