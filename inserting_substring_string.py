str=input('enter a string: ')
sub=input('enter a sub string: ')
n=int(input('enter position no: '))
n-=1
l1=len(str)
l2=len(sub)
str1=[]
for i in range(n):
    str1.append(str[i])
for i in range(l2) :
    str1.append(sub[i])
for i in range(n,l1):
    str1.append(str[i])
str=''.join(str1)
print(str1)