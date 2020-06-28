# 2. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.

def stringrepeat(usr_input):
    if len(usr_input) >= 2:
        print (usr_input[0:2] + usr_input[-2:])
    else:
        print ("Empty String")


data = input("Enter string:")
stringrepeat(data)
