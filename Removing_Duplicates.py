str = input("Enter a String : ")

Ans = ''
stack = ''

for ch in str:
    if ch in stack:
        continue
    else:
        stack = stack + ch
        Ans = Ans + ch

print(Ans)