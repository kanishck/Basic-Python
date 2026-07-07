text = input("Enter a string: ")

count={}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

for ch in count.keys():
    if count[ch] == 1:
        print("First non repeating character is:", ch)
        break


