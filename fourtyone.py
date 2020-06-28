# 41. Write a Python program to convert a tuple to a string.
def tuple_to_string(data):
    print(data)
    str = ''.join(data)
    print (str)


input_string = input("Enter three character without space:  ")
val = tuple(input_string)
tuple_to_string(val)
