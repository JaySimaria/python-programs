#aliasing an array
from numpy import *
a=arange(1,6)#create a with elements 1to5
b=a #give another name b to a

print('original array: ',a)
print('alias array: ',b)
b[0]=99 #modify 0th element of b
print('after modification: ')
print('original array: ',a)
print('alias array: ',b)