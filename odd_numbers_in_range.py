#6-7-22
#odd numbers in range
start, end = 10, 20

# iterating each number in list
for num in range(start, end + 1):

    # checking condition
    if num % 2 != 0:
        print(num, end=" ")