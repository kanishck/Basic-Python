sent = input("Enter a string : ")

alpha=0
digit=0
count=0

for ch in sent:
    if ch.isalpha():
        alpha+=1
    if ch.isdigit():
        digit+=1
    if not ch.isalpha() and not ch.isdigit():
        count+=1

print("alphabetic characters : ", alpha)
print("Digits : ", digit)
print("Neither Alphabetic nor Digits : ", count)

if '@' in sent or '#' in sent:
    print("Contains Special Symbol")
else:
    print("No Special Symbol Found")