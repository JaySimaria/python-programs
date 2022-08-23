# 5-8-22
# check if two array are equal or not
def areequal(arr1, arr2, j, s):

    if(j !=s):
        return False

    # sort both array
    arr1.sort()
    arr2.sort()

    # linearly compare
    for i in range(0,j):
        if(arr1[i] != arr2[i]):
            return False

    # If all elements are same
    return True

# Driver Code
if __name__ == "__main__":
        arr1 = [3, 5, 2, 5, 2]
        arr2 = [2, 3, 5, 5, 2]
        j = len(arr1)
        s = len(arr2)

        if (areequal(arr1, arr2, j, s)):
            print("Yes")
        else:
            print("No")

