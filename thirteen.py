# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
#
input_string = input("Enter a list elements separated by space: ")
words = [word for word in input_string.split(",")]
print(",".join(sorted(list(set(words)))))
# listToStr = ' '.join([str(elem) for elem in res])
# print(listToStr)

