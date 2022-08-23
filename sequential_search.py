#28-1-22
#searching an array for an element
from array import *
#creating an empty array to store integers
x=array('i',[])
#store elements into the array x
print('how many elements? ', end=' ')
n=int(input())#accept input into n
for i in range(n): #repeat for n times
    print('enter element: ',end=' ')
    x.append(int(input())) #add the element to the array
print('Original array: ',x)
print('enter element to search: ',end=' ')
s=int(input()) #accept element to be searched
#linear search or sequential search
flag=False #this becomes True if element is found
for i in range(len(x)): #repeat i from 0 to no. of elements
    if s==x[i]:
        print('found at position= ',i+1)
        flag=True
if flag==False:
    print('Not found in the array')
