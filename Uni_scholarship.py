perc = float(input("Enter your percentage: "))
income = float(input("Enter your family income: "))
scholarship = 0

if perc < 75:
    print("You are not eligible for any scholarship.")
else :

    print("You are eligible for scholarship.")
    
    if perc >= 75 and perc < 80:
        print("General Scholarship")
        if income < 200000:
            scholarship = 100
        elif income >= 200000 and income < 500000:
            scholarship = 50
        else:
            scholarship = 25

    elif perc >= 80 and perc < 90:
        
        print("Academic Scholarship")
        
        if income < 200000:
            scholarship = 100
        elif income >= 200000 and income < 500000:
            scholarship = 50
        else:
            scholarship = 25
    
    elif perc >= 90:
        
        print("Merit Scholarship")
        
        if income < 200000:
            scholarship = 100
        elif income >= 200000 and income < 500000:
            scholarship = 50
        else:
            scholarship = 25
    
    print("Your scholarship amount is:", scholarship,"%")