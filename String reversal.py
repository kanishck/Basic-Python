text = input("Enter the string : ")

reversed = ''

for ch in text:
    reversed = ch + reversed 

print(reversed)
