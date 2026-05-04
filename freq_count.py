l=[1,3,3,3,2,2]
freq={}
for i in l:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)