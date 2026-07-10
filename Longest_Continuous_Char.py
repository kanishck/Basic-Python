# 10. Find the longest continuous sequence of the same character and print the character along with
# its count.

text = input("Enter the string : ")

count=0
max_count=0
char = text[0]

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        if count > max_count:
            max_count = count
            char = text[i-1]
        count = 1
print(char)
print(max_count)