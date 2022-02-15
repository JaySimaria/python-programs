#28-1-22
#searching an array for an element - v2.0
from array import*
#create an empty array to store integers
x=array('i',[])

#store elements into the array x
print('how many elements? ',end=' ')
n=int(input())#accept input into n
for i in range(n): #repeat for n times
    print('enter element: ',end=' ')
    x.append(int(input())) #add the element  to the array x
print('original array: ',x)

print('enter element to search: ',end=' ')
s=int(input())#accept element to be searched
#index() method gives the location of the element in the array
try:
    pos=x.index(s)
    print('found at position=',pos+1)
except valueerror:# if element not found then valueerror will else\
    print('not found in the array')