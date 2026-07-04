str = input("Enter a String : ")

Ans = ''

for i in range(0,len(str)-1):
    
    if str[i] == str[i+1]:
        continue
    else:
        Ans = Ans + str[i]

Ans += str[-1]

print(Ans)