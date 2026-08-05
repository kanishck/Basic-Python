# From 100 to 200 print palindrome numbers without using string

for num in range(100,201):
    last = num%10
    first = num//100

    if first == last:
        print(num, end=' ')
