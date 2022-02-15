#28-1-22
#sorting an array using bubble short technique
from array import*
#create an empty array to store integers
x=array('i',[])

#store elements into the array x
print('how many elements? ',end=' ')
n=int(input())#accept input into n

#store elements into the array x
print('how many elements? ',end=' ')
n=int(input()) #accept input into n

for i in range(n): #repeat for n times
    print('enter element: ',end=' ')
    x.append(int(input())) # add the element to the array x
print('original array: ',x)

#bubblesort
flag = False # when swapping is done, flag becomes true
for i in range(n-1): # l is from 0 to n-1
    for j in range(n-1-i): # j is  from 0 to one element lesser than i
        if x[j] > x[j+1]: #it lst element is  bigger than the 2nd one
            t=x[j]#swap j and j+1 elements
            x[j]=x[j+1]
            x[j+1]=t
            flag=true #swapping done, hence flag is true
    if flag==False: #no swapping means array is in sorted order
         break #come out of inner for loop
    else:
         flag=false #assign initial value to flag
print('sorted array= ',x)      