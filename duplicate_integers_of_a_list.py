#5-7-22
#print duplicates integers from a list

lst=[1,1,5,5,7,7,20,20,80,80,15,15,7,7,9,9,40,70,40,80,99,80,80,100,100]
J=[]
S=[]
for i in lst:
    if i not in J:
        J.append(i)
for i in J:
    if lst.count(i) > 1:
        S.append(i)
        print(S)
