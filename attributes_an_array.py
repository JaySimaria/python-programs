#31-1-22
#the ndim attribute
from numpy import array
arr1=array([1,2,3,4,5])# 1d array
print(arr1.ndim)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.ndim)

#the shape attribute
arr1=array([1,2,3,4,5])
print(arr1.shape)           

arr2=array([[1,2,3],[4,5,6]])
print(arr2.shape)

arr2.shape=(3,2) #change shape of arr2 to 3 rows and 2 cols
print(arr2)

# the size attribute
arr1=array([1,2,3,4,5])
print(arr1.size)
