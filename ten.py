# 10. Write a Python program to remove the characters which have odd index
# values of a given string.
def truncate_odd_index(str):
    result = ''
    for i in range(len(str)):
        if i % 2 == 1:
            result = result + str[i]
    return result


usr_input = input("Enter the string: ")
print(truncate_odd_index(usr_input))
