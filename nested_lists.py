# To create a list with another list as element
list = [10,20,30, [80,90]]
print('Total list= ',list) # display entire list
print('First element= ',list[0]) #display first element
print('Last element is nested list= ',list[3]) #display nested list
for x in list[3]: #display all elements in nested list
    print(x)

