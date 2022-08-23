#to know the result of comparing two arrays
from numpy import *
a=array([1,2,3,0])
b=array([0,2,3,1])

c=a==b
print('result of a==b: ',c)
c=a>b
print('result of a>b: ',c)
c=a<=b
print('result of a<=b',c)


#using any() and all() functions
from numpy import *
a=array([1,2,3,0])
b=array([0,2,3,1])

c=a<b
print('result of a<b: ',c)

print('check if any one element is true: ',any(c))
print('check if all elements are true: ',all(c))

if(any(a>b)):
    print('a contains atleast one element greater than those of b')


#using logical_and(),logical_or(),logical_not()
from numpy import *
a=array([1,2,3],int)
b=array([0,2,3],int)

c=logical_and(a>0,a<4)
print(c)
c=logical_or(b>=0,b==1)
print(c)

c=logical_not(b)
print(c)


#using where() function
from numpy import *
a=array([10,20,30,40,50,],int)
b=array([1,21,3,40,51],int)
#if a>b then make element from a else from b
c=where(a>b,a,b)
print(c)



#using nonzero() function
from numpy import *
a=array([1,2,0,-1,0,6],int)
#retrieve includes of non zero elements from a
c=nonzero(a)
#display indexes
for i in c:
    print(i)
#display the elements
print(a[c])

