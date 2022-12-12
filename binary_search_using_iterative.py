# 12- 12- 2022
# binary search using iterative
def binarySearch(v, To_Find):
	lo = 0
	hi = len(v) - 1

	# This below check covers all cases , so need to check
	# for mid=lo-(hi-lo)/2
	while hi - lo > 1:
		mid = (hi + lo) // 2
		if v[mid] < To_Find:
			lo = mid + 1
		else:
			hi = mid

	if v[lo] == To_Find:
		print("Index found", lo)
	elif v[hi] == To_Find:
		print("Index found ", hi)
	else:
		print("Not Found")


if __name__ == '__main__':
	v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	To_Find = 5
	binarySearch(v, To_Find)

	To_Find = 10
	binarySearch(v, To_Find)

	To_Find = 1
	binarySearch(v, To_Find)


