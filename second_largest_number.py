#29-6-22
# Python program to find largest number
# in a list

# List of numbers
list1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Removing duplicates from the list
list2 = list(set(list1))

# Sorting the list
list2.sort()

# Printing the second last element
print("Second largest element is:", list2[-2])
