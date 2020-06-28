# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.
def value_exchanger(data):
    return data[-1:] + data[1:-1] + data[:1]


usr_input = input("Enter string value : ")
print(value_exchanger(usr_input))
