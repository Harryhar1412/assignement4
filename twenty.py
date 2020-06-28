# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

def start_end_same(items):
    c = 0
    for x in items:
        if len(x) >= 2:
            if x[0] == x[-1]:
                c += 1
    return c


input_string = input("Enter a list elements separated by space: ")
userList = input_string.split()
print (start_end_same(userList))
