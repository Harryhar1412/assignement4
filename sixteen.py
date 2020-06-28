# 16. Write a Python program to sum all the items in a list
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
# print (userList)
print (sum_list(userList))
