# 21-7-22
# to print all positive integers in a range
# input string
start = int(input("enter a starting range: "))
end = int(input("enter a ending range: "))
# iterating each number
for num in range(start,end+1):

    # checking condition
    if num >= 0:
        print(num, end=" ")
