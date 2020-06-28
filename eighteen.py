# 18. Write a Python program to get the largest number from a list.
def largest(items):
    lg = items[0]
    for x in items:
        if lg < x:
            lg = x
    return lg


input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
# print (userList)
print (largest(userList))
