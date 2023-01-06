# 27-12-22
# shell sort example 1
from math import floor


def shellSort(arr):
    n = len(arr)
    # Gap sequence
    gap = floor(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Compare elements at equal gap.
            while j >= gap and temp < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = floor(gap / 2)


arr = [3, 2, 1, 4, 6, 9, 5, 10, 0]
shellSort(arr)
print(arr)
