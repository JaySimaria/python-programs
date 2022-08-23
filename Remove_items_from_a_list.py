#9-7-22
#remove items from a list
def remove(initial_set):
    while(initial_set):
        initial_set.pop()
    print(initial_set)

#Driver code
initial_set = set([10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
remove(initial_set)