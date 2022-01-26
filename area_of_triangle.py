j=9
s=6
y=4
b=7
r=2
#uncomment below to take inputs from the user
#j=float(input('enter first side:'))
#s=float(input('enter second side:'))
#j=float(input('enter third side:'))
#j=float(input('enter fourth side:'))
#j=float(input('enter fifth side:'))

#calculate the semi-perimeter
s=(j+s+y+b+r) / 2

#calculate the area
area=(s*(s-j)*(s-s)*(s-y)*(s-b)*(s-r)) ** 0.5
print('the area of the triangle is %0.2f' %area)
