emp_code = input("Enter the employee code : ")

if(emp_code.isalnum()):
    print(emp_code.upper())
else:
    print("Invalid Employee Code")
    