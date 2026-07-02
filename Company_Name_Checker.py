comp_name = input("Enter the company name : ")
comp_name = comp_name.title()

print("Title Case : ", comp_name)
count = 0
comp_name=comp_name.upper()

for i in range(0,len(comp_name)):
    if comp_name[i] == 'A': 
        count += 1
        if comp_name[i+1] == 'I':
            count += 1
            flag = 1

print("charaters found : ", count)

if flag > 0:
    print("AI related name")

