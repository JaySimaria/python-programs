#19-7-22
#cloning or copying
def cloning(list1):
    list_copy=[]
    list_copy=list1
    return list_copy
#Drivercode
list1=[10,15,20,25,30,35,40,45,50]
list2=cloning(list1)
print("original list: ",list1)
print("After cloning: ",list2)