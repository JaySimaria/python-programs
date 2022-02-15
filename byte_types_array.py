# program to understand bytes type array
# create a list into byte numbers
elements=[10,20,30,40,50,60,70,80]
#convert the list into bytes type array
x=bytes(elements)
#retrieve elements from x using for loop and display
for i in x:
    print(i)