# python program to find the factorial of a number provided by the user .

# change the value for a different result
num=7
# To take input from the user
# num = int(input("Enter the number:"))

factorial = 1
# Check if the number is negative , positive and zero 
if num<0:
    print("Sorry , factorial doees not exit for negative numbers")
elif num==0:
    print(" The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print(" The factorial of ",num,"is",factorial)