# Reverse a string without using any inbuilt function or slicing

str = 'apple'
str2 = ''

for i in range(1,(len(str)+1)):
    str2+=str[-i]

print(str2)

# Second method
rev=''

for ch in str:
    rev = ch + rev

print(rev)