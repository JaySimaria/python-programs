#inserting a new element into a tuple
names=('Vishnu','Anupama','Lakshmi','Bheeshma')
print(names)

#accept new name and position number
lst=[input('Enter a new name: ')]
new=tuple(lst)
pos= int(input('enter position no: '))

#Copy from 0th to pos-2 into another tuple names 1
names1= names[0:pos-1]
names1= names1+new

#concatenate the remaining elements of names from pos-1 till end
names=names+names[pos-1:]
print(names)
     