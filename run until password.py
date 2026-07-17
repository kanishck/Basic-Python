userset = 123456
count = 0
while(count < 5):
    inp = int(input(" Enter the password : "))
    if inp != userset:
        count += 1
        print("Incorrect Password")
        if count==5:
            print("Try again in a few minutes")
    else :
        print("Logged IN")
        break
