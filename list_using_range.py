#creating lists using range() function
# create a list with 0 to 9 consecutive integer numbers
list1 = range(10)
for i in list1: # display element by element
    print(i,', ', end='')
print() #throws cursor to nest line

#create list with integers from 5 to 9
list2= range(5,10)
for i in list2:
    print(i, ',',end='')
print()
         
#create a list with odd numbers from 5 to 9
list3= range(5,10,2) #step size is 2
for i in list3:
    print(i, ',', end='')
    
    
#displaying list of elements using while and for loop
list=[10,20,30,40,50,60]

print('using while loop')
i=0
while i<len(list): # repeat from 0 to length of list
    print(list[i])
    i=i+1
    print('Using for loop')
    for i in list: #repeat for all elements
        print(i)
        