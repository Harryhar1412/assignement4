# 39. Write a Python program to unpack a tuple in several variable
def tuple_unpack(data):
    a = data
    (first, second, third) = a
    print(first)
    print(second)
    print(third)


input_string = input("Enter three character without space:  ")
val = tuple(input_string)
tuple_unpack(val)
