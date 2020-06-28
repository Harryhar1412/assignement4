# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.
def prefix_text(li_data, text):
    res = ["{}{}".format(text, i) for i in li_data]
    return (res)


input_string = input("Enter Prefix List : ")
userList = input_string.split()
str = input("text that Need to manipulate: ")
print (prefix_text(userList, str))
