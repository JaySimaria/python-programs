# 10-2-23
# to print any number of multiplication
for number in range(1, 51):
    if (number % 7) != 0:
        # the current number is not a multiple of 7, so continue until the next number
        continue

    print(f'{number} is a multiple of 7')
