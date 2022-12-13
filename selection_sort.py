# 13-12-2022
# selection sort
# time complexity O(n*n)
# sorting by finding min_index
def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


arr = [100,95,69,48,90,33,6,34,88,90,9,85,66,50,55,5,1]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
