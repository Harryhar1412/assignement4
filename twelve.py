# 12. Write a Python script that takes input from the user and displays that input
# back in upper and lower cases

def upper_text(str_value):
    res = str_value.upper()
    return res


usr_input = input("Enter The string value: ")
print (upper_text(usr_input))
