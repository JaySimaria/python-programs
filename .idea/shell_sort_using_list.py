# 26-12-22
# shell sort list
def ShellSort(array):
    inter = len(array) // 2
    while inter >= 1:
        i = 0
        while i < inter:
            j = i + inter
            while j < len(array):
                if array[j] < array[j - inter]:
                    array[j], array[j - inter] = array[j - inter], array[j]
                j = j + inter
            i = i + 1
        inter = inter // 2

array1 = [8, 9, 2, 0, 7, 1, 6, 4, 3, 5]
ShellSort(array1)
print(array1)