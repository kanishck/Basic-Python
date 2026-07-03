str = input("Enter a string : ")

vow=0
cons=0

vowels = 'aeiouAEIOU'

for ch in str:
    if ch in vowels:
        vow+=1
    elif ch.isalpha():
        cons+=1

print(vow)
print(cons)