s = ["Apple"]

s="PINEAPPLE"   

print(s[0::2])

print(s[-7:-9:-1])


#String Formatting
name = "vijay"
age = 24

formatted_string = f"My name is {name}. My age is {age}."
print(formatted_string)

formatted_string = "My name is {}. My age is {}.".format(name, age)
print(formatted_string)

# String operators
first_name = 'Vishal'
last_name = 'Dubey'

full_name = first_name + ' ' + last_name
print(full_name)

# * operator
print('vinay' * 100)

#Membership Operator
text = 'This is a sentence'
print('T' in text)

# Iterating over strings
# for( int i =0;i<=5; i++)


for i in range(0,6): # starting index is inclusive, ending index is exclusive
    print(i)

s = 'this is a sentence'

for i in range(0, len(s)):
    print(s[i])

for ch in s:
    print(s)

