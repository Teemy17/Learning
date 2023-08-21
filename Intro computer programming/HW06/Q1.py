from datetime import datetime

def time_24_to_12(time) :
    dateTime = datetime.strptime(time, '%H:%M')
    time = dateTime.strftime('%I:%M %p').lstrip('0')
    return time


print(time_24_to_12("23:24"))

# Another version using if else.

 def time_24_to_12_2(time) :
     hours, minute = time.split(":")
     if int(hours) > 12:
         return (f"{int(hours) - 12}:{minute} PM")
     elif int(hours) >= 12:
         return (f"{int(hours)}:{minute} PM")
     else:
         return (f"{int(hours)}:{minute} AM")

 print(time_24_to_12_2("23:24"))
