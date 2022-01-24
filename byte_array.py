#program to understand bytearray type array
#create a list of byte numbers
elements=[10,20,30,40,50]
#convert the list into byte array type array
x=bytearray(elements)
#modify the first two numbers
x[3]=75
x[4]=45
#retrieve elements from x using for loop and display
for i in x:
    print(i)
