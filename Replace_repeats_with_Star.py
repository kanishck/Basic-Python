text = input("Enter the string : ")

str1 = ''
ans = ''

for ch in text:
    if ch in str1:
        ans += '*'
    else:
        ans += ch
        str1 += ch

print(ans)
print(str1)