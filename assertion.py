#26-3-22
#understanding assert statement
x=int(input('enter a number greater than 0: '))
assert x>0,"wrong input entered"
print('U entered: ',x)




#to handle assertion error raised by assert\
x=int(input('enter a number greater than 0:'))
try:
    assert(x>0) # exception may occur here
    print('u entered:',x)
except assertionerror:
    print("Wrong input entered")# this is executed in case of
    #exception    

