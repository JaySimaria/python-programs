# sum of natural numbers up to num
num = 25

if num < 0:
    print("enter the positive number")
else:
    sum = 0
    # use while loop to iterate   until zero
    while(num > 0):
     print("Current num value is {0} & sum value is {1}: ".format(num, sum))
     sum += num
     num -= 1
    print("The sum is",sum)
     