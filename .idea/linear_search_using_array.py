# 4-1-2023
# linear search array
def linear_search(arr, a, b):

    # Going through array
    for i in range(0, a):
        if (arr[i] == b):
            return i
    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The array given is ", arr)
b = 80
print("Element to be found is ", b)
a = len(arr)
index = linear_search(arr, a, b)
if(index == -1):
    print("Element is not in the list")
else:
    print("Index of the element is: ", index)