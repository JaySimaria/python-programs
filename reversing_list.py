#27-8-22
# Python code
#To reverse list

#input list
lst=[10,20,30,40,50,60,70,80,90,100]
# the above input can also be given as
# lst=list(map(int,input().split()))
l=[] # empty list
# checking if elements present in the list or not
for i in lst:
    #reversing the list
    l.insert(0,i)
# printing result
print(l)
