# 15-12-22
# bubblesort simple program
def bubble_sort(nlist):
    for i in range(len(nlist) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if nlist[j + 1] < nlist[j]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                no_swap = False
        if no_swap:
            return

#input list
alist = [1, 74, 96, 5, 42, 63]
print('Input List\n', alist)

#sort list
bubble_sort(alist)
print('Sorted List\n', alist)