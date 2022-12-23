# 23-12-22
# quick sort using list
def quicksort(list, start, end):
    # Sorts the list from indexes start to end - 1
    if end - start > 1:
        p = partition(list, start, end)
        quicksort(list, start, p)
        quicksort(list, p + 1, end)


def partition(list, start, end):
    pivot = list[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and list[i] <= pivot:
            i = i + 1
        while i <= j and list[j] >= pivot:
            j = j - 1

        if i <= j:
            list[i], list[j] = list[j], list[i]
        else:
            list[start], list[j] = list[j], list[start]
            return j


list = input('Enter the list of numbers: ').split()
list = [int(x) for x in list]
quicksort(list, 0, len(list))
print('Sorted list: ', end='')
print(list)