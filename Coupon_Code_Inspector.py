code = input("Enter the coupon code : ")

if code.isalnum():
    print("Valid Coupon")
else:
    print("Invalid Coupon")

count = 0

for ch in code:
    if ch.isupper():
        count += 1

print(count)