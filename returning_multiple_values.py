def sum_sub(a,b):
    """ This function returns results of addition and substraction of a,b """
    c=a+b
    d=a-b
    return c,d
x,y = sum_sub(10,5)
print("result of addition: ",x)
print("result of subtraction: ",y)

def sum_sub_mul_div(a,b):
    """ this function returns results of addition ,subtraction,multiplication and division of a,b """
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f
t=sum_sub_mul_div(10,5)
print('The results are: ')
for i in t:
    print(i,end=', ')
