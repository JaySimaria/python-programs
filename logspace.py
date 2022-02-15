#29-1-12
#creating an array using logspace()
from numpy import *
#divide the range: 10 power 1 to 10 power 4 into 5 equal parts
#and take those points in the array
a= logspace(1,4,5)
#find no. of elements in a
n=len(a)
#repeat from 0 to n-1 times
for i in range(n):
    print('%.1f' %a[i],end=' ')#display 1 digit after decision point