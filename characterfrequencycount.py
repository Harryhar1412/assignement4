# 1.Write a Python program to count the number of characters (character
# frequency) in a string.
val = input("Enter a word For counting Character frequency:")
frequency = {}
d = {}
for i in val:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
# print (frequency)
sort_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
d = {i[0]: i[1] for i in sort_frequency}
print(d)
# print(type(sort_frequency))
# print (sort_frequency)

# =========================================================================
