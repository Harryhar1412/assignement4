# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
def questionno5():
    data = input("enter The Value: ")
    if len(data) > 2:
        if data[-3:] == 'ing':
            data += 'ly'
        else:
            data += 'ing'
    return data


result = questionno5()
print(result)
