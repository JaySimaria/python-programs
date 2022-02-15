str=[]
n=int(input('how many strings?'))
for i in range(n):
    print('enter string: ',end=' ')
    str.append(input())
    str1=sorted(str)
    print('sorted list: ')
    for i in str1:
        print(i)
