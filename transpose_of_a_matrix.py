from numpy import*
r,c=[int(a) for a in input("enter rows,cols: ").split()]
str=input('enter matrix elements:\n')
x=reshape(matrix(str),(r,c))
print('the original matrix: ')
print(x)
print('the transpose matrix: ')
y=x.transpose()
print(y)