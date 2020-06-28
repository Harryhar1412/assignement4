# 3.Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.


def chgcharacter_position(usr_input):
    c = usr_input[0]
    usr_input = usr_input.replace(c, '$')
    usr_input = c + usr_input[1:]
    return usr_input


data = input("Enter String:")
res=chgcharacter_position(data)
print (res)