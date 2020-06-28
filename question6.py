# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

def negetioncase(data):
    notstr=data.find('not')
    strafter=data.find('poor')
    if strafter > notstr:
        data = data.replace(data[notstr:(strafter + 4)], 'good')

    return data

usr_input=input("Enter as statement including Not: ")
res=negetioncase(usr_input)
print(res)