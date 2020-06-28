# 15. Write a Python function to insert a string in the middle of a string.
def new_string(data, text):
    # a = len(data) / 2
    val = data[:2] + text + data[2:]
    return val


string_first_last = input("Enter The String for First and Last: ")
string_middle = input("Enter The String In Middle of another String: ")
print (new_string(string_first_last, string_middle))
