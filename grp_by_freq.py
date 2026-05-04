nums=[1,1,2,2,3]
res={}
for n in nums:
    res.setdefault(n,[]).append(n)
print(res)