word1 = input("Enter the first string : ")
word2 = input("Enter the second string : ")
is_anagram = True
for ch in word1:
    if ch not in word2:
        is_anagram = False

if is_anagram:
    print("The strings are Anagrams")
else:
    print("Not anagrams")