# 23=7-22
# print all negative integers of a range
start = int(input("enter the starting range: "))
end = int(input("enter the ending range: "))
# iterating the number
for num in range(start,end+1):

    # if checking condition
    if num < 0:
        print(num, end=" ")


