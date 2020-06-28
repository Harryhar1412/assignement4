# 1. Write a Python function to find the Max of three numbers.
def max_find(x,y,z):
    if x>y and x>z:
        return x
    elif y>z and y>x:
        return y
    else:
        return z
ui1=int(input("Enter first Number :"))
ui2=int(input("Enter second Number :"))
ui3=int(input("Enter third Number :"))
print(max_find(ui1,ui2,ui3))
