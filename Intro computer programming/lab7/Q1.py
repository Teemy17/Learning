class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def func(self):
        return (f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs")

time1 = Time(9, 30, 0)
print(time1.func())
