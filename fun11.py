# 11. Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.
r = lambda a : a + 15
user_val=int(input("enter a Number : "))
print(r(user_val))
h=int(input("Enter a Number : "))
i=int(input("Enter a Number : "))
r = lambda x, y : x * y
print(r(h, i))