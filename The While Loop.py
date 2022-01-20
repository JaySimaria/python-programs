#To Display Even Numbers Between M and N
m,n=[int(i) for i in input("enter minimum and maximum range:").split(',')]
x=m #Start From M Onwards
if x % 2!=0: #If x is not even,start from next number
    x=x+1
while x>=m and x<=n:
    print(x)
    x+=2


