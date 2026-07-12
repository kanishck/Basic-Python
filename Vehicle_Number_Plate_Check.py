v_num = input("Enter the vehicle number : ")

flag = False
sum_dig = 0

if v_num[-1] != '0':
    if v_num[:2].isupper() and v_num[:2].isalpha():
        if v_num[-4:].isdigit():
            for ch in v_num[-4:]:
                sum_dig += int(ch)
            if sum_dig%2 == 0:
                flag = True      
if flag:
    print("Entry Allowed")
else:
    print("Entry Denied")