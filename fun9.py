# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
def test_prime(n):
    if (n==1):
        return "Nope"
    elif (n==2):
        return "Prime"
    else:
        for x in range(2,n):
            if(n % x==0):
                return "Nope"
        return "Prime"

usr_input=int(input("enter a Number to check Prime or not:"))
print(test_prime(usr_input))