# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
def truncate_repeat(data):
    dup_items = set()
    uniq_items = []
    for x in data:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    return (uniq_items)


input_string = input("Enter a list elements separated by space ")
userList = input_string.split()
print (truncate_repeat(userList))