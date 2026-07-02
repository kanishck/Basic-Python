emp_code = input("Enter the employee code : ")

digit = 0

if(emp_code.isalnum()):
    print(emp_code.upper())
    for ch in emp_code:
        if ch.isdigit():
            digit+=1
    print(digit)
else:
    print("Invalid Employee Code")
