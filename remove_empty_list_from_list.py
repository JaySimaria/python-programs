#5-6-22
#remove empty list from list
# Initializing list by custom values
lst=[10,20,30,40,50,[],[],[]]
#printing original list
print("The original list is: "+str(lst))
#Remove empty list to list
#using filter method
res = list(filter(None, lst))

# Printing the resultant list
print("List after empty list removal : " + str(res))
