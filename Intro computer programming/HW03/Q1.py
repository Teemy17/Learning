name =  str(input("Enter Employee's name: "))
hours = float(input("Enter number of hours work in a week: "))
pay_rate = float(input("Enter hourly paty rate: "))
fedtax = float(input("Enter federal tax withholding rate: "))
sttax = float(input("Enter state tax withholding rate: "))

gross = hours * pay_rate
fed_withhold = gross * fedtax
st_withhold = gross * sttax
total_ded = fed_withhold + st_withhold
net_pay = gross - total_ded

print(f"\nEmployee name: {name}")
print(f"Hours work: {hours}")
print(f"Pay rate: ${pay_rate}")
print(f"Gross pay: ${gross}")
print("Deductions: \n   "
    f"Federal withholding ({fedtax * 100}%) : ${fed_withhold} \n   "
    f"State withholding ({sttax * 100}%) : ${st_withhold} \n   "
    f"Total Deduction : ${total_ded}"
    )
print(f"Net pay : ${net_pay}")