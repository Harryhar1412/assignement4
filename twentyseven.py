# 27. Write a Python program to replace the last element in a list with another list.
def replace_last_by_list(data, new_list):
    # last_item=data[-1]
    res = data[:-1] + new_list
    return (res)


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
second_list = input("Enter a list elements separated by space ")
userList1 = second_list.split()
print (replace_last_by_list(userList, userList1))
