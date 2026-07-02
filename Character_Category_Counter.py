s = input("Enter the string : ")

alpha =0
digit=0
upper=0
lower=0

for ch in s:
    if ch.isalpha():
        alpha += 1
    if ch.isdigit():
        digit += 1
    if ch.isupper():
        upper += 1
    if ch.islower():
        lower += 1

print(f"alphabetic characters : {alpha} \n digits : {digit} \n uppercase letters : {upper} \n lowercase letters : {lower}")