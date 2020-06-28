# 31. Write a Python program to iterate over dictionaries using for loops.
def dict_loop(data):
    dict = {data[i]: data[i + 1] for i in range(0, len(data), 2)}
    for key, value in dict.items():
        print(key, 'corresponds to ', dict[key])


newsDictData = input("Enter a list elements separated by space: ")
userList = newsDictData.split()
dict_loop(userList)
