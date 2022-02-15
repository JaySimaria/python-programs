# Modifying an existing element of aa tuple
num=(10,20,30,40,50)
print(num)

#accept new element and position number
lst=[int(input('Enter a new element: '))]
new=tuple(lst)
pos=int(input('Enter position no: '))

#copy from oth to pos-2 into another tuple num1
num1=num[0:pos-1]

#concatenate new element at pos-1
num =num1+new

# concatenate the remaining elements of num from pos till end
num=num1+num[pos:]
print(num)