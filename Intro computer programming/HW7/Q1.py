import time
class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def set_time(self, hr, min, sec):
        self.hour = hr
        self.minute = min
        self.second = sec
    
    def display_time(self):
        if self.hour > 12:
         return (f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} PM")
        elif self.hour >= 12:
         return (f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} PM")
        else:
         return (f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} AM")
        
    def get_time(self):
        return (f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
    
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0

        

c = Clock(13,49,55) 
while True:
    print(c.display_time())
    c.tick()
    time.sleep(1)  

        
