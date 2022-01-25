#searching for an element in a list
group1 = [1,2,3,4,5] #take a list of elements
search = int(input('enter element to search: '))
for element in group1:
    if search == element:
        print('element found  in group1')
        break # come out of for loop
else:
    print('element not found in group1') #this is a suite