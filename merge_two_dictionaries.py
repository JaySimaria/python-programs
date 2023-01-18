# 17-1-23
# merge two dictionaries

def merge(dict1, dict2):
    result = dict1 | dict2  # merge operator (|)
    return result


dict1 = {'A': 'Jay ', 'B': 'Messi ', 'C': 'Ronaldo'}
dict2 = {'D': 'Hardik Pandiya ', 'E': 'Rishabh pant', 'F': 'Kohli'}
print(merge(dict1, dict2))  # print dict3
