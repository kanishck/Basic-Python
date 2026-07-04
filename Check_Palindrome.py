text = input("Enter a String : ")

rev=''

for ch in text:
    rev = ch + rev

if rev==text:
    print(" Palindrome ")
else:
    print("Not a Palindrome")