# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters
def string_test(data):
    up=0
    lc=0
    for c in data:
        if c.isupper():
           up+=1
        elif c.islower():
           lc+=1
        else:
           pass
    print ("Original String : ", data)
    print ("No. of Upper case characters : ", up)
    print ("No. of Lower case Characters : ", lc)

usr_input=input("Enter String value:")
string_test(usr_input)
