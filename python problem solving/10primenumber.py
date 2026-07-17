num = int(input("Enter a number : "))
flag = 1 
for i in range(2, num):
    if(num%i == 0):
        flag = 0
        print("not a prime number")
        break


if(flag==1):
    print("Its a prime number")

    