import matplotlib.pyplot as plt

def list_to_string(input_list):
    string = ""
    for num in input_list:
        string = string + str(num)
    return string

def find_occurance(string):
    result = {}
    for number in string:
        if number.isdigit():
            result[number] = result.get(number,0) + 1
    return result

def autopct_format(l):   
    result = find_occurance(list_to_string(l))
    values = list(result.values())
    total = sum(values)
    def my_format(pct):
        absolute = int(pct/100.*total)
        return f"({absolute})"
    return my_format

def draw_pie_chart(l):
    result = find_occurance(list_to_string(l))
    num = list(result.keys())
    value = list(result.values())
    plt.pie(value, labels=num, autopct= autopct_format(l), startangle=180)
    plt.show() 

l = [3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3]
draw_pie_chart(l)
