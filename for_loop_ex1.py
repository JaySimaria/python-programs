# 27-1-23
# sum of list of elements using for loop
# creating the list of numbers
numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]

# initializing a variable that will store the sum
sum = 0

# using for loop to iterate over the list
for num in numbers:
    sum = sum + num ** 2

print("The sum of squares is: ", sum)
