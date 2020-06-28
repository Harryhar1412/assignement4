# 19. Write a Python program to get the smallest number from a list.
def smallest(items):
    sm = items[0]
    for x in items:
        if sm > x:
            sm = x
    return sm


input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
# print (userList)
print (smallest(userList))