# 40. Write a Python program to add an item in a tuple.
def add_item_in_tuple(data):
    data=data+(20,)
    print (data)
input_string = input("Enter three character without space:  ")
val = tuple(input_string)
add_item_in_tuple(val)