N = 5
listN = []
for i in range(0,5) :
    listN.append(0)
sum=0
list = [1,2,1,2,1,2,4]
for i in range(0, len(list)) :
    listN[list[i]-1]+=1
for i in range(0,5) :
    if listN[i] != 0 :
        sum += 1
print(sum)
