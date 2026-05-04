nums=[2,4,3,5,7,8]
t=7
pairs=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==t:
            pairs.append((nums[i],nums[j]))
print(pairs)