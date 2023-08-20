from datetime import datetime

def time_24_to_12(time) :
    dateTime = datetime.strptime(time, '%H:%M')
    time = dateTime.strftime('%I:%M %p').lstrip('0')
    return time


print(time_24_to_12("23:24"))


