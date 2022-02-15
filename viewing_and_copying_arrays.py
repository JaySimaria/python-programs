#29-1-22
#creating view for an array
from numpy import *

a=arange(1,6)#create a with elements 1 to 5
b=a.view() #create a view of a and call it b
print('original array: ',a)
print('new array: ',b)

b[0]=99 #modify 0th element of b
print('after modification: ')
print('original array: ',a)
print('new array: ',b)


#copying an array
from numpy import *
a= arange(1,6) # create a with elements 1 to 5
b=a.copy() #create a copy of a and call it b
print('original array: ',a)
print('new array: ',b)

b[0]=99 #modify 0th element of b
print('after modification: ')
print('original array: ',a)
print('new array: ',b)
