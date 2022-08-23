#18-7-22
# remove dictionary key words
# Using split() + loop + replace()

# initializing string
test_str = 'Believe In Yourself '

# printing original string
print("The original string is : " + str(test_str))

# initializing Dictionary
test_dict = {'Believe' : 1, 'In': 6}

# Remove Dictionary Key Words
# Using split() + loop + replace()
for key in test_dict:
	if key in test_str.split(' '):
		test_str = test_str.replace(key, "")

# printing result
print("The string after replace : " + str(test_str))
