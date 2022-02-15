#1-2-22
#retrieving the elements from a 2D array using indexing
from numpy import *

#create a 2D array with 3 rows and 3 Cols
a=[[1,2,3],[4,5,6],[7,8,9]]

#display only rows
for i in range(len(a)):
    print(a[i])
    
#display element by element
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end=' ')
            
    
#retrieving the elements from a 3D array using indexing
from numpy import *
#create a 3D array with size 2x2x3
a=[[[1,2,3],
    [4,5,6]],
   
   [[7,8,9],
   [10,11,12]]]

#display element by element
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i] [j])):
            print(a[j][j][k],end='\t')
        print()
    print()    