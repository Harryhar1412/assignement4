# 36. Write a Python program to sum all the items in a dictionary.
def sum_dict(data):
    my_dict = {data[i]: data[i + 1] for i in range(0, len(data), 2)}
    a = sum(my_dict.keys())
    b = sum(my_dict.values())
    return (a + b)


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
print(sum_dict(userList))
