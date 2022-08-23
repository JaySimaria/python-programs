#program to display fibonacci series
n=int(input('how many fibonaccis ?'))
f1=0 #this is first fibonacci no
f2=1 # this is second one
c=2  # counts the no of fibonaccis
if n==1:
    print(f1)
elif n==2:
    print(f1,'\n',f2,aug=' ')
else:
    print(f1,'\n',f2,sep=' ')
    while c<n:
        f=f1+f2 # add two fibonaccis to get  the new one
        print(f)
        f1,f2=f2,f #this is same as f1=f2 ,f2=f
        c+=1 #increment counter