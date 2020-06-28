# 30. Write a Python script to check whether a given key already exists in a
# dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
user_input=int(input("enter The Value Key: "))

is_key_present(user_input)