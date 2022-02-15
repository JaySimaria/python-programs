#to find sum of the list of members using while - v2.0
#take a list of numbers\
list=[10,20,30,40,50,60,70,80,90,100]
sum=0 #initally sum is zero
i=0 #take a variable
while i<len(list):
    print(list[i]) #display the element from list
    sum+=list[i] #add each element to sum
    i+=1
print('sum=',sum)    
    
    