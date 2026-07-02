usrname = input("Enter the Username : ")
flag = 0

for ch in usrname:
    if (not ch.isalpha()):
        flag = 1
        print("Invalid Username!")
        break
if (flag == 0):
    print(usrname.upper())