# 24. Write a Python program to clone or copy a list.
import copy


def copy_clone(data):
    print (data)
    # return (copy.copy(data))
    return (copy.deepcopy(data))


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
print (copy_clone(userList))
