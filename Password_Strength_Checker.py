pwd = input("Enter the password : ")

upper=0
lower=0
digit=0

if len(pwd) < 8:
    print("Minimum 8 characters!!")
else:
    for ch in pwd:
        if(ch.isupper()):
            upper += 1
        elif(ch.islower()):
            lower += 1
        elif(ch.isdigit()):
            digit +=1

    if upper>=1 and lower >=1 and digit >= 1:
        print("Strong Password")
    else:
        print("Weak Password")