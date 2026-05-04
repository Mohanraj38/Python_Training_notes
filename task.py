#swap two numbers
a=5
b=10
c=a
a=b
b=c
print(a,b)

#length of a string
str1="Mohanraj"
print(len(str1))

#print 1st and last element  of list
arr=[1,2,3,4,5,6,7]
print(arr[0],arr[-1])

#vowel count
s="abdeu"
v="aeiou"
c=0
for i in s:
    if i in v:
        c+=1
print(c)

#sum of element in a list
arr=[1,2,3,4,5,6,7]
s=0
for i in arr:
    s+=i
print(s)

#max in a list
arr=[1,12,3,44,5,60,7]
maxi=-999999
for i in arr:
    if i>maxi:
        maxi=i
print(max)

#print even number
arr2=[1,2,3,4,5,6,7,8]
for i in arr2:
    if i%2==0:
        print(i)

#count words
sr="hi how r u"
c=0
for i in sr:
    if i==' ':
        c+=1
print(c+1)

#celsius to farenheit
c=int(input("enter in celcius"))
f=(c*(9/5))+32
print(f)

#palindrome
ss="madam"
ss1=ss
rev=""
for i in range(len(ss1)-1,-1,-1):
    rev+=ss[i]
if ss==rev:
    print("Palindrome")
else:
    print("Not Palindrome")