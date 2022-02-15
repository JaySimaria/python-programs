def prime(n):
    """ to check if n is prime or not """
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x
num=int(input('enter a number: '))
result=prime(num)
if result ==1:
    print(num,'is prime')
else:
    print(num,'is not prime')

def prime(n):
    """ to check if n is prime or not """
    x=1
    for i in range(2,n):
        if n%i == 0:
            x=0
        break
    else:
        x=1
    return x

num=int(input('How many primes do you want'))
i=2
c=1
while True:
    if prime(i):
        print(i)
        c+=1
    i+=1
    if c>num :
        break


