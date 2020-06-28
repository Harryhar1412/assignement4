# 17. Write a Python program to multiplies all the items in a list.
def mul_list(items):
    mul_numbers = 1
    for x in items:
        mul_numbers *= x
    return mul_numbers


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
# print (userList)
print (mul_list(userList))
