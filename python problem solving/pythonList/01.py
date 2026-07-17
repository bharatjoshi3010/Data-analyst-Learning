a = ["rose", "rachel", "monika", "joe"]
# swapping the postion of rose and joe
a[0], a[3] = a[3], a[0]
print(a)

# add a new value at second position
a.insert(2,"bharat")
print(a) 

#remove element from 3rd pos
a.pop(3)
print(a)

b = [4, 5, 6, 2]


# multiplie all the elements of the list 
mul=1
for i in b:
    mul = mul*i

print(mul)

#lageset number form list
max = b[0]
for i in b:
    if(i>max):
        max=i

print(max)

# or 

b.sort()
# print(b[len(b)-1])
print(b[-1])

#smallest value 
print(b[0])