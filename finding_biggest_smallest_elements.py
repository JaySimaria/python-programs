# finding biggest and smallest numbers in a list of numbers
x=[] # take an empty list

print('how many elements? ' , end='')
n=int(input()) #accept input into n

for i in range(n): #repeat for n times
    print('Enter element: ',end='')
    x.append(int(input())) #add the element to the list x
print('The list is: ',x) #display the list
big=x[0] # initially Oth element becomes maximum and minimum
small=x[0]

for i in range(1,n): # repeat from 1 to n-1 elements
    if x[i]>big: big=x[1] # if any other element is > big, take it as #big
    if x[i]<small:small=x[i] # if any other element is small,take it as small
    
print('Maximum is: ',big) #display max and min elements
print('Minimum is: ',small)