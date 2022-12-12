# 11-12-2022
# linear search
def linear_Search(list1, n, key):
    # Searching list1 sequentially
    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 10

n = len(list1)
res = linear_Search(list1, n, key)
if (res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)