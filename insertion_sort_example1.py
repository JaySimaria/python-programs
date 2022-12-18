# 18-12-22
# insertion sort
def InSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Algorithm Implementation
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Take Users Input
n = int(input("Mention the number of elements in the array : "))
arr = []
print("Enter the elements in the array")
for i in range(0, n):
    # m represents the elements of the array
    m = int(input())
    arr.append(m)

# Display array before sorting
print("Array before Sorting :")
print(arr)

InSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])