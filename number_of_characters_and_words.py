str=input('enter a string: ')
i=0
for s in str:
    print(str[i],end=' ')
    i+=1
print('\nNO. of characters: ',i)

str=input('enter a string: ')
i=c=0
flag=True
for s in str:
    if flag==False and str[i]==' ':
        c+=1
if str[i]==' ':
    flag=True
else:
    flag=False
i+=1
print('no of words: ',c+1)


