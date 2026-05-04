data={'a':25,'b':15,'c':30}
m=-999999
c=''
for i,j in data.items():
    if j>m:
        m=j
        c=i
print(m,c)