#4-2-22
def sum(a,b):
    """ This function finds sum of two numbers """
    c=a+b
    return c
x=sum(10,15)
print('the sum is: ',x)
y=sum(1.5,10.75)
print('the sum is: ',y)


def even_odd(num):
    """ to know num is even or odd """
    if num % 2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
even_odd(12)
even_odd(13)

def fact(n):
    """ to find factorial value """
    prod=1
    while n>=1:
        prod*=n
        n-=1
        return prod
for i in range(1,11):
    print('factorial of {} is {}'.format(i,fact(i)))

