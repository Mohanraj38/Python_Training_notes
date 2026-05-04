nums=[4,5,1,2,0,4]
freq={
}
for n in nums:
    freq[n]=freq.get(n,0)+1
for n in nums:
    if freq[n]==1:
        print(n)
        break