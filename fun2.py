# 2. Write a Python function to sum all the numbers in a list.
def sum_list(data):
    sum_numbers = 0
    for x in data:
        sum_numbers += x
    return sum_numbers
usr_input=input("Enter first Number :")
userList=usr_input.split()
for i in range(0, len(userList)):
    userList[i] = int(userList[i])
print (sum_list(userList))
