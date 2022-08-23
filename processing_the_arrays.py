#operations on arrays
from array import*

#create an array with int values
arr = array('i',[10,20,30,40,50])
print('original array: ',arr)

#append 30 to the array arr
arr.append(30)
arr.append(60)
print('after appending 30 and 60:',arr)

#insert 99 at position number 1 in arr
arr.insert(1,99)
print('after inserting 99 in 1st position: ',arr)

#remove an element from arr
arr.remove(20)
print('after removing 20: ',arr)

#remove last element using pop() method
n=arr.pop()
print('array after pop(): ',arr)
print('popped element:',n)

#finding position of element using index() method
n=arr.index(30)
print('first occurence of element 30 is at: ',n)

#convert an array into a list using tolist() method
lst=arr.tolist()
print('list: ',lst)
print('array: ',arr)


from array import *
#accept marks from keyboard into a list
lst = [int(i) for i in input('enter marks: ').split(',')]
#create an integer array from the above list
marks=array('i',lst)
#display the marks and find total
sum=0
for x in marks:
    print(x)
    sum+=x
print('total marks: ',sum)
#display percentage
n=len(marks) # n=no. of elements in marks array
percent =sum/n
print('percentage: ',percent)
