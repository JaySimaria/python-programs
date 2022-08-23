#17-7-22
#sorted dict by key or value
# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'Jalpa': '10', 'Dharmesh': '9',
		'Sarthi': '15', 'Bandana': '2', 'Jay': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)
