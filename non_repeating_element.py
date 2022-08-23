# 5-8-22
#non=repeating elements
# Python3 program to find first
# non-repeating element.

def firstNonRepeating(arr, n):
    for i in range(n):
        j = 0
        while (j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        if (j == n):
            return arr[i]

    return -1


# Driver code
arr = [10, 20, 30, 30, 30, 40, 50, 40, 50, 70, 80, 100, 100]
n = len(arr)
print(firstNonRepeating(arr, n))


