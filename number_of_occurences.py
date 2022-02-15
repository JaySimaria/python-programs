#counting how many times an element occurred int he list
x=[] # take an empty list

n= int(input('How many elements? ')) #accept input into n

for i in range(n): #repeat for n times
    print('Enter element: ',end='')
    x.append(int(input())) #add the element to the list x
print('The list is: ',x) #display the list

y=int(input('Enter element to count: '))
c=0
for i in x:
    if(y==i): c+=1
print('{} is found {} times.'.format(y,c))
    

