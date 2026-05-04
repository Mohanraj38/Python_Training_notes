num=[1,2,4,5]
n=len(num)+1
n1=len(num)
total_sum=n*(n+1)//2
actual_sum=0
for i in num:
    actual_sum=actual_sum+i
miss=total_sum-actual_sum
print(miss)


