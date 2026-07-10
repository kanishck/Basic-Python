std_reg = input("Enter the registration number : ")

flag = True

if (std_reg[:2] != "CS" and std_reg[:2] != "IT") :
    print("Invalid Registration Number")
else:
    if std_reg[-3:].isdigit() :
        dig_sum = int(std_reg[-3:])
        if not (dig_sum >= 101 and dig_sum <= 300):
            flag = False
    else:
        flag = False
if flag:
    print("Valid Registration Number")
else: 
    print("Invalid Registration Number")