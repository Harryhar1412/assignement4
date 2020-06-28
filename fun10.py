# 10. Write a Python program to print the even numbers from a given list.
def evn_num(data):
    newdat = []
    for i in data:
        if i % 2 == 0:
            newdat.append(i)
    print (newdat)


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
print (evn_num(userList))
