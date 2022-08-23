#30-6-22
# Python3 code to demonstrate working of
# Tuple summation
# Using list() + sum()

# initializing tup
tuples = (10, 11, 12, 13, 14, 15)

# printing original tuple
print("The original tuple is : " + str(tuples))

# Tuple elements inversions
# Using list() + sum()
res = sum(list(tuples))

# printing result
print("The summation of tuple elements are : " + str(res))
