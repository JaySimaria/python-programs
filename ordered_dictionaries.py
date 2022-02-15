#create an ordered dictionary
from collections import OrderedDict
d=OrderedDict() # d is ordered dictionary
d[10]='A'
d[11]='B'
d[12]='C'
d[13]='D'

#display the ordered dictionary
for i,j in d.items():
    print(i ,j)