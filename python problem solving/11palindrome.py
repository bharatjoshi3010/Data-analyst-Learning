num = input("Enter a number : ")

digit = len(num)
num = int(num)
stnum= num
newnum = 0
for i in range(digit, 0, -1):
    newnum = (num%10)*(10**(i-1))+newnum
    num = num//10

print("its a palindrome") if(newnum == stnum) else print ("not a palindrome")