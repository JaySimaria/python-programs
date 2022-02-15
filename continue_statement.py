# 26-1-22
#using continue to execute next iteration of while loop
x=0
while x<10:
    x+=1
    if x>5: # if x>5 then continue next iteration
        continue
    print('x= ',x)
print("out of loop")