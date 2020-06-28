# 38. Write a Python program to remove a key from a dictionary

def remove_key(data,keytoremove):
    my_dict = {data[i]: data[i + 1] for i in range(0, len(data), 2)}
    print (my_dict)
    if keyremove in my_dict:
        del my_dict[keyremove]
    print (my_dict)

input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
keyremove=int(input("Input a number  as key  "))
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
remove_key(userList,keyremove)