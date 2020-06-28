# 4. Write a Python program to reverse a string.
def reverse_fun(data):
    str = ""
    for i in data:
        str = i + str
    return str
usr_input=input("enter The string to reverse: ")
print (reverse_fun(usr_input))