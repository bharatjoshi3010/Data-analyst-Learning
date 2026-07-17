n = int(input("Enter the value of n : "))

p=1
q=1

for i in range(1, n):
    if(i==1 or i==2):
        print("1")
    else:
        print(p+q)
        m=q
        q=p+q
        p=m
