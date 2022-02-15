#29-1-22
#mathematical_operations on arrays
#import all from nuumpy module
from numpy import *

#create a numpy array using array() function
arr=array([10,20,30.5,-40])
print("original array:",arr)

#do arithmetic operations on the elements of the array
print("after adding 5: ",arr+5)
print("after subtracting 5:" ,arr-5)
print("after multiplying with 5: ",arr*5)
print("after dividing with 5: ",arr/5)
print("after modulas with 5: ",arr%5)

#we can use the arrays in expression also
print("expression value: ",(arr+5)**2-10)
#do some math function
print("sin values: ",sin(arr))
print("cos values: ",cos(arr))
print("tan values: ",tan(arr))
print("biggest element: ",max(arr))
print("smallest element: ",min(arr))
print("sum of all elements: ",sum(arr))
print("average of all elements: ",mean(arr))