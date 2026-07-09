text = input("Enter the string : ")

str1=''
str2=''

for ch in text:
    if ch.isdigit():
        str1 = str1 + ch
    else:
        str2 = str2 + ch

print(str2+str1)
