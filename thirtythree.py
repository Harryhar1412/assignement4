# 33. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

d = dict()

for x in range(1,15+1):
    d[x]=x*x

print(d)