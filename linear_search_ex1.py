# 3-1-23
# binary search example
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['p','y','t','h','o','n','3']
x = '3'
print("element found at index "+str(linearsearch(arr,x)))