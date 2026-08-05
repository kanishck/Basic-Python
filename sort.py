
li = [1,5,3,6,2,3]

for i in range(len(li)):
    for j in range(len(li)-1):
        if li[j]>li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp

print(li)