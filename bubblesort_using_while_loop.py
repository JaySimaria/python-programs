# 15-12-22
# bubble sort using while loop
# create a empty list
a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element : " %i))
    a.append(value)

i = 0
while i < number -1:
    j = 0
    while j < number - i - 1:
        if a[j] > a[j + 1]:
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp
        j = j + 1
    i = i + 1

print("The List in Ascending Order : ", a)

