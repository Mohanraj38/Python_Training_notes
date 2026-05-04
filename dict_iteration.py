Student={
    "name":"rahul",
    "ages":22,
    "city": "chn"
}
del Student["name"]
print(Student)

#keys iteration
for keys in Student:
    print(keys)

#value iter
for values in Student.values():
    print(values)

#loop key,value pair
for keys,value in Student.items():
    print(keys,value)