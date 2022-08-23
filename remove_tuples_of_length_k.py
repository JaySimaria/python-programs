#30-6-22
# Python3 code to demonstrate working of
# Remove Tuples of Length K
# Using filter() + lambda + len()

# initializing list
test_lis00t = [(1, ), (3, ), (5, 6, 7), (8, ), (9, 10, 11, 12)]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 1

# filter() filters non K length values and returns result
res = list(filter(lambda x : len(x) != K, test_list))

# printing result
print("Filtered list : " + str(res))
