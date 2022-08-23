# 26-3-22
# using pass to do nothing
x=0
while x<10:
    x+=1
    if x>5: # if x>5 then continue next iteration
        pass
    print('x= ',x)
print("out of loop")



#retrieving only negative numbers from a ist
num=[1,2,3,-5,-6,-7,-8,-9,10,11,12,13,14,15]
for i in num:
    if(i>0):
        pass # we are not interested\
    else:
        print(i) #this is what we need
