sent = input("Enter sentence : ")

if sent[0].islower():
    sent = sent.upper()

count = 0
vowels = 'AEIOU'

for ch in sent:
    if (ch.isalpha() and ch not in vowels):
        count +=1

print(sent)
print(count)