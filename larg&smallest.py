num = 12654334639
large = num % 10
small = num % 10

while num != 0:
    digit = num%10
    if digit > large:
        large = digit
    if digit < small:
        small = digit
    num //= 10

print(large,"\n", small)