#5-2-22
a=1
def myfunction():
    a=2
    print('a= ',a)
myfunction()
print('a= ',a)

a=1
def myfunction():
    global a
    print('global a= ',a)
    a=2
    print('modified a= ',a)
myfunction()
print('global a= ',a)

a=1
def myfunction():
    a=2
    x=globals()['a']
    print('global var a=',x)
    print('local var a= ',a)
myfunction()
print('global var a=',a)