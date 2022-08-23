#12-7-22
# find the sum of all items in dict

# Function to print sum


def returnSum(dict):

	sum = 0
	for i in dict.values():
		sum = sum + i

	return sum


# Driver Function
dict = {'j': 500, 'd': 400, 'b': 300}
print("Sum :", returnSum(dict))
