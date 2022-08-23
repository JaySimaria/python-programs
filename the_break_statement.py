x=10
while x>=1:
    print('x= ',x)
    x-=1
print("out of loop")





#using break to come out of while loop
x=10
while x>=1:
    print('x= ',x)
    x-=1
    if x==5: # if x is 5 then come out from while loop
        break
print("out of loop")