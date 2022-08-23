#4-7-22
#simple interest
def simple_interest(p,t,r):
    print("the principal is",p)
    print("the time period is",t)
    print("the rate of interest",r)

    si=(p*t*r)/100

    print("the simple interest is",si)
    return si

#driver code
simple_interest(9,1,9)
