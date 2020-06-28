# 23. Write a Python program to check a list is empty or not.
def check_list_empty(data):
    l = []
    if data == l:
        return ("List is empty")
    else:
        return data


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
print (check_list_empty(userList))
