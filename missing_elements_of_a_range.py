# 4-8-22
# A hashing based Python3 program to
# find missing the elements of a range

# Print all elements of range
# [low, high] that are not
# present in arr[0..n\
def printMissing(arr, n, low, high):

# Insert all elements of
# arr[] in set
    s = set(arr)

# Traverse through the range
# and print all missing elements
    for x in range(low, high + 1):
        if x not in s:
            print(x, end = ' ')

# Driver Code
arr = [10, 40, 50, 100, 150]
n = len(arr)
low, high = 11, 100
printMissing(arr, n, low, high)

