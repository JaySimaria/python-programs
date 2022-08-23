# Python3 code to demonstrate
# Swap elements in String list
# using replace() + list comprehension

# Initializing list
test_list = ['I', 'love', 'python', 'programming', 'languages']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]

# printing result
print ("List after performing character swaps : " + str(res))
