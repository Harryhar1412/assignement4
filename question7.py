# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.

def logest_listitem(listeargs):
    find_length = []
    for n in listeargs:
        find_length.append((len(n)))
    find_length.sort()

    return find_length[-1]


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
print(logest_listitem(userList))
