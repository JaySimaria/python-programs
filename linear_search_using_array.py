# 11-12-22
# linear search using array
# Linear Search in Python


def linearSearch(array, n, x):

    # array using sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = 100
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)