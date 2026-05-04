num=[0,1,0,3,12]

index=0
for i in range(len(num)):
    if num[i]!=0:
        num[index]=num[i]
        index+=1
for i in range(index,len(num)):
    num[i]=0
print(num)