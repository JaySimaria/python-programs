# 7-1-22
# list example
# Taking one variable and integer
a = 20
# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)  # adding the element
print(lst)