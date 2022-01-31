#31-1-22
#slicing an array
from numpy import *
#create array with elements 10 to 15
a=arange(10,16)
print(a)

#retrieve from 1st to ine element prior to 6th element in steps of 2
b=a[1:6:2]
print(b)

#retrieve all elements from a
b=a[::]
print(b)

#retrieve from 6-2=4th to one element prior to 2nd element in
#decreasing step size
b=a[-2:2:-1]
print(b)

#retrieve from 0th to one element prior to 4th element (6-2=4th)
b=a[:-2:]
print(b)


#indexing an array
from numpy import *
a=arange(10,16)
print(a)
#retrieve from 1st to one element prior to 6th element in steps of 2
a=a[1:6:2]
print(a)

#display elements using indexing
i=0
while(i<len(a)):
    print(a[i])
    i+=1



