# 37. Write a Python program to multiply all the items in a dictionary.

def mul_dict(data):
    my_dict = {data[i]: data[i + 1] for i in range(0, len(data), 2)}
    a = 1
    for key, value in my_dict.items():
        a = key * my_dict[key] * a
    return a

input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
print(mul_dict(userList))
