num = int(input("Enter the number : "))
rev=0
temp = num
while num!= 0 :
    print(num)
    rev *= 10 
    rev += num%10
    num //= 10

print(rev)
if rev == num:
    print("Palindrome !!")