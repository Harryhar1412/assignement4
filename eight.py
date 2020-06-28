# 8. Write a Python program to remove the nthindex character from a nonempty
# string
def truncate_char(str, n):
    starttext = str[:n]
    endtext = str[n + 1:]
    return starttext + endtext


input_string = input("Enter String value: ")
pos = int(input("Enter the Position: "))
print(truncate_char(input_string, pos))
