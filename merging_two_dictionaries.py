#17-7-22
# merging two dictionaries
# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return (dict1.update(dict2))


# Driver code
dict1 = {'j': 20, 'r': 10}
dict2 = {'b': 15, 'y': 7}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict1)
