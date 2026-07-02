pwd = input("enter password")

upper = 0
lower = 0
digits = 0

for ch in pwd:
    if(ch.isupper()):
        upper = upper + 1
        continue

    elif(ch.islower()):
        lower = lower + 1
        continue
    
    elif(ch.isdigit()):
        digits = digits + 1
        continue


print(f"uppercase - {upper}")
print(f"lowercase - {lower}")
print(f"digits - {digits}")

if (upper > 0 and lower > 0 and digits > 0):
    print("Strong Password")
else:
    print("Weak Password")