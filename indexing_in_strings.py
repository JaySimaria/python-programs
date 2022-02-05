#indexing on strings
str='core python'
n=len(str)  # n = no.of chars in str
i=0
while i<n:
    print(str [i],end=' ')
    i+=1
print()
i=-1
while i>=-n:
    print(str[i],end =' ')
    i-=1
print()
i=1
n=len(str)
while i<=n:
    print(str[-i],end=' ')
    i+=1


str='core python'
for i in str:
    print(i,end=' ')
print()
for i in str[:: -1]:
    print(i,end=' ')






