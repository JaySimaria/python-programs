#7-2-22
f=lambda x: x*x
value=f(5)
print('square of 5=',value)

f=lambda x,y:x+y
result=f(1.55,10)
print('sum= ',result)

max=lambda x,y: x if x>y else y
a,b=[int(n) for n in input("enter two numbers:").split(',')]
print('bigger number= ',max(a,b))


def is_even(x):
    if x%2==0:
        return True
    else:
        return False
lst=[10,23,45,56,70,59]
lst1=list(filter(is_even,lst))
print(lst1)

lst=[10,23,45,46,70,99]
lst1=list(filter(lambda x:(x%2==0),lst))
print(lst1)

def squares(x):
    return x*x
lst=[1,2,3,4,5]
lst1=list(map(squares,lst))
print(lst1)

lst=[1,2,3,4,5]
lst1=list(map(lambda x: x*x,lst))
print(lst)

lst1=[1,2,3,4,5]
lst2=[10,20,30,40,50,60,70,80,90,100]
lst3=list(map(lambda x,y: x*y,lst1,lst2))
print(lst3)

from functools import*
lst=[1,2,3,4,5]
result=reduce(lambda x,y: x*y,lst)
print(result)