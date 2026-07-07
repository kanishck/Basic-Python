import math

num = int(input("Enter an integer : "))

is_prime = True

if(num%2==0 or num%3==0):
    is_prime = False

for i in range(5, int(math.sqrt(num))):
    if num%i == 0:
        is_prime = False

if is_prime:
    print("Prime Number!!")
else:
    print("Not Prime!!")
