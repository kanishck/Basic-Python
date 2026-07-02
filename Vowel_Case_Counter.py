sent = input("Enter a Sentence : ")

L_vowels = ['a','e','i','o','u']
U_vowels = ['A','E','I','O','U']

upper_vow = 0
lower_vow = 0

for ch in sent:
    if ch in L_vowels:
        lower_vow += 1
    elif ch in U_vowels:
        upper_vow += 1

print(f"Upper case : {upper_vow}")
print(f"Lower case : {lower_vow}")