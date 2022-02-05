#5-2-22
#positional arguments
def attach(s1,s2):
    """ to join s1 and s2 and display total string """
    s3=s1+s2
    print('Total string: '+s3)
attach ('new','york')

#keyword arguments
def grocery(item,price):
    """ To display the given arguments """
    print('Item = %s' %item)
    print('Price = %2.f' %price)
grocery(item='sugar',price=50.75)
grocery(price=88.00,item='oil')

#default arguments
def grocery(item,price=40.00):
    """to display the given arguments """
    print('item=%s'%item)
    print('price=%.2f'%price)
grocery(item='sugar',price=50.75)
grocery(item='sugar')

#variable length arguments
def add(farg,*args):
    """ to add given numbers """
    print('formal arguments= ',farg)
    sum=0
    for i in args:
        sum+=i
    print('sum of all numbers= ',(farg+sum))
add(5,10)
add(5,10,20,30)

def display(farg,**kwargs):
    """to display given values """
    print('formal argument= ',farg)
    for x,y in kwargs.items():
        print('key={},value={}'.format(x,y))
display(5,rno=10)
print()
display(5,rno=10,name='Jay')  
          
