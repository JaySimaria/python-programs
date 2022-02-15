#accessing elements of an array using index
from array import *
x=array('i',[10,20,30,40,50,60,70,80,90,100])
#find number of elements in the array
n=len(x)
#dispay array elements using indexing
for i in range(n): # repeat from 0 to n-1
    print(x[i],end=' ')
    
#accessing elements of an array using index -v 2.0
from array import *
x=array('i',[10,20,30,40,50,60])
#find number of elements in the array
n=len(x)
#display array elements using indexing
i=0
while i<n:
    print(x[i],end=' ')
    i+=1
    
    
    
#creating array y with elements from 1st to 3rd from x
y=x[1:4]
print(y)
#create array y with elements from 0th till the last element in x
y=x[0:]
print(y) 
#create array y with elements from oth to 3rd from x
y=x[:4]
print(y)
#create array y with last 4 elements from x
y=x[-4:]
print(y)
#create y with last 4th element and with 3[-4-(-1)=-3]elements
#towards fight
y=x[-4:-1]
print(y)
#create y with 0th to 7th elements from x
#stride 2 means,after 0th element,retrieve every 2nd element from x
y=x[0:7:2]
print(y)


# using slicing to display elements of an array
from array import *
x=array('i',[10,20,30,40,50,60,70])
#display elements from 2nd to 4th only
for i in x[2:5]:
    print(i)

    
    