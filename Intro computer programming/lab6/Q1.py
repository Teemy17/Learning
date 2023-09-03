def getGrade(score) : 
    if 100 >= score >= 80.0:
        grade = "A"
    elif  80 > score >= 70.0:
        grade = "B"
    elif 70 > score >= 60.0:
        grade = "C"
    elif 60 > score >= 50.0:
        grade = "D"
    elif 0 <= score < 50:
        grade = "F"
    elif score > 100:
        grade = "invalid"
    else:
        grade = "invalid"
    return grade


print(getGrade(36))
print(getGrade(80))
print(getGrade(101))
print(getGrade(55))
print(getGrade(67))
print(getGrade(75))
print(getGrade(-5))
print(getGrade(0))