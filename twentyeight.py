# 28. Write a Python script to add a key to a dictionary.
def dict_keyaddd(data,newdata):
    dictionary={data[i]: data[i + 1] for i in range(0, len(data), 2)}
    print(dictionary)
    dict1={newdata[i]: newdata[i + 1] for i in range(0, len(newdata), 2)}
    dictionary.update(dict1)
    print(dictionary)
input_string = input("Enter a list elements separated by space: ")
newsDictData = input("Enter a list elements separated by space: ")
userList = input_string.split()
keywordnew = newsDictData.split()
dict_keyaddd(userList,keywordnew)
