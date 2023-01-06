# 26-12-22
def shell_sort(array, n):
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = array[i]
            j = i
            while j >= h and array[j - h] > t:
                array[j] = array[j - h]
                j -= h

            array[j] = t
        h = h // 2


array = [34, 12, 20, 7, 13, 15, 2, 23]
n = len(array)
print('Array before Sorting:')
print(array)
shell_sort(array, n)
print('Array after Sorting:')
print(array)