# # reverse a string
s = input("enter a string : ")
# for i in range(len(s)-1, -1, -1):
#     print(s[i], end="")
## or
# print(s[::-1])              #you can even store it as a string, so also helps in checking palindrome


# if a string contaians only digits
# s = input("enter a string : ")
# print(s.isnumeric())

# # chechk if a string is palindrome
# s = input("enter a string : ")
# k = ""
# flag= 1
# for i in range(0, int(len(s)/2)):
#     if(s[i] != s[len(s)-1-i]):
#         flag =0
#         break
# print("its a palindrome") if (flag) else print("not a palindrome")


# #check number of vowel in a string
# s = input("enter a string : ")
# count =0
# for i in range(0, len(s)):
#     if s[i] in ("aeiouAEIOU"):
#         count +=1
# print("The number of vowel in the string : ",count)

#is first letter of each word is capital or not ?
# s = input("enter a string : ")
# print(s.istitle())
