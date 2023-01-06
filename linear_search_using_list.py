# 4-1-23
# linear search using list
def linear_search(list, key):
    """Return index of key in alist. Return -1 if key not present."""
    for i in range(len(list)):
        if list[i] == key:
            return i
    return -1


list = input('Enter the list of numbers: ')
list = list.split()
list = [int(x) for x in list]
key = int(input('The number to search for: '))

index = linear_search(list, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))