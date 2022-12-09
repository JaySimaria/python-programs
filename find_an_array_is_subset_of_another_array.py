# 9-12-22
# find an array is subset of another array
# Return 1 if arr2[] is a subset of arr1[] */


def isSubset(arr1, arr2, m, n):
	i = 0
	j = 0
	if m < n:
		return 0

	arr1.sort()
	arr2.sort()

	while i < n and j < m:
		if arr1[j] < arr2[i]:
			j += 1
		elif arr1[j] == arr2[i]:
			j += 1
			i += 1
		elif arr1[j] > arr2[i]:
			return 0
	return False if i < n else True


# Driver code
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n) == True:
	print("arr2 is subset of arr1 ")
else:
	printf("arr2 is not a subset of arr1 ")


