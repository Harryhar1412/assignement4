# 29. Write a Python script to concatenate following dictionaries to create a new
# one.
# def concating_dict(data, newdata):
    # dictionary = {data[i]: data[i + 1] for i in range(0, len(data), 2)}
    # print (dictionary)
    # dict1 = {newdata[i]: newdata[i + 1] for i in range(0, len(newdata), 2)}
    # dictionary.update(dict1)
    # print (dictionary)
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


# input_string = input("Enter a list elements separated by space: ")
# newsDictData = input("Enter a list elements separated by space: ")
# userList = input_string.split()
# keywordnew = newsDictData.split()
# concating_dict(userList, keywordnew)
