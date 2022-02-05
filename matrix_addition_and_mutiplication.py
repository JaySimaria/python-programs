# matrix multiplication
import sys
from numpy import*
r1,c1=[int(a) for a in input("first matrix rows,cols: ").split()]
r2,c2=[int(a) for a in input("second matrix rows,cols: ").split()]
if c1!=r2:
    print('multiplication is not possible')
    sys.exit()
str1=input('enter first matrix elements:\n')
x=reshape(matrix(str1),(r1,c1))
str2=input('enter second matrix elements:\n')
y=reshape(matrix(str2),(r2,c2))
print('the product matrix:')
z=x*y
print(z)