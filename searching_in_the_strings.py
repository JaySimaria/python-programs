#3-2-22
str=[]
n=int(input('how many strings? '))
for i in range(n):
    print('enter string: ',end=' ')
    str.append(input())
s=input('enter string to search: ')
flag=False
for i in range(len(str)):
    if s==str[i]:
        print('found at: ',i+1)
        flag=False
if flag==False:
    print('not found')


