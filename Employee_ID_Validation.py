emp_ID = input("Enter the Employee ID : ")

# if len(emp_ID) == 7 and emp_ID[:3].isupper() and emp_ID[3:].isdigit() :
#     print("Valid Employee ID")
# else:
#     print("Invalid Employee ID")

start = emp_ID[0:3]
end = emp_ID[-4:]
digit = True
upper = True

for i in range(len(start)):
    if not end[i].isdigit():
        digit = False
    if not start[i].isupper():
        upper = False
    if digit and upper:
        print('Valid employee ID')
    else:
        print("Invalid Employee ID")