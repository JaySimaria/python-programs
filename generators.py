def mygen(x,y):
    while x<=y:
        yield x
        x+=1
g=mygen(5,10)
for i in g:
    print(i,end=' ')

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
g= mygen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
    