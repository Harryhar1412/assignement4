# 20. Write a Python program to find intersection of two given arrays using
# Lambda
n1 = [1, 2, 3, 5, 7, 8, 9, 10]
n2 = [1, 2, 4, 8, 9]
print("Original arrays:")
print(n1)
print(n2)
result = list(filter(lambda x: x in n1, n2))
print ("\nIntersection of the said arrays: ",result)