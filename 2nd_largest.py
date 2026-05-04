a=[10,20,4,45,99]
m=-9999
for i in a:
    if i>m:
        m=i
m1=-9999
for i in a:
    if i>m1 and i<m:
        m1=i
print(m1)
