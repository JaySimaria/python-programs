#5-2-22
def factorial(n):
    """ to find factorial of n """
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
for i in range(1,11):
    print('factorial of {} is {}'.format(i,factorial(i)))
    
def towers(n,a,c,b):
    if n==1:
        print('move disk %i from %s to pole %s' %(n,a,c))
    else:
        towers(n-1,a,b,c)
        print('move disk %i from pole %s to pole %s'%(n,a,c))
        towers(n-1,b,c,a)
n=int(input('enter number of disks:'))
towers(n,'A','C','B')
    