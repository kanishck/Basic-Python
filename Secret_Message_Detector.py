msg = input("Enter the message : ")

msg = msg.swapcase()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
num = 0

for ch in msg:
    if ch in vowels:
        num += 1
print(num)
