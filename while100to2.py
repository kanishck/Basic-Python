num = int(input("Enter the number : "))
prime = True
i = 2
while (i*i<num):
    if num%i == 0:
        prime = False
    i += 1
if prime:
    print("Prime")
else:
    prime("Not Prime")