# 24-12-22
# quick sort example1

def quick_sort(alist, start, end):
    # Sorts the list from indexes start to end - 1 inclusive
    if end - start > 1:
        p = partition(alist, start, end)
        quick_sort(alist, start, p)
        quick_sort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


# input list
alist = [1, 74, 96, 5, 42, 63]
print('Input List\n', alist)

# sort list
quick_sort(alist, 0, len(alist))
print('Sorted List\n', alist)