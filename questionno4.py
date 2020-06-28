# 4.Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.

def swap(usr_input1, usr_input2):
    output1 = usr_input2[:2] + usr_input1[2:]
    output2 = usr_input1[:2] + usr_input2[2:]
    return output1 + '  ' + output2

data1 = input("First String: ")
data2 = input("Second String: ")
res=swap(data1, data2)
print(res)