code = input("Enter the Product Code : ")
sum_digits = 0 
Val = True

if len(code) != 6:
    print("Invalid Product code")
else: 
    if not code[:2].isupper():
        Val = False
    if not code[-4:].isdigit():
        Val = False
    for ch in code[-4:]:
        sum_digits += int(ch)
    if sum_digits <= 15:
        Val = False
    if Val:
        print( "Valid Product Code")
    else:
        print("Invalid Product Code")