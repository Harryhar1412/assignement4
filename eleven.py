# 11. Write a Python program to count the occurrences of each word in a given
# sentence

def occurance_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


usr_input = input("Enter the Sentance to Cout the Occurance of Word: ")
print(occurance_count(usr_input))
