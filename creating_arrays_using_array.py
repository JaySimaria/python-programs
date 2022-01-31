#28-1-22
#creating an array with characters
from numpy import *
arr=array(['delhi','hyderabad','mumbai','ahmedabad']) #create array
print(arr)#display array


#creating an array from another array
from numpy import *
a=array([1,2,3,4,5])#original array
b=array(a)#create b from a using array() function
c=a #create c by assigning a to c
#display the arrays
print("a= ",a)
print("b= ",b)
print("c= ",c)
