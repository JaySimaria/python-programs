#program to evaluates exponential seres
#accept user input
x,n=[int(i)  for i in input("enter power of e, no. of iterations: ").split(',')]
#this become the first term
t=1
#till now,find the sum
sum=t
#display the iteration number and sum
print('Iteration=%d\tsum=%f'%(1,sum))
#repeat for 1st to n-1th terms
for j in range(1,n):
        t=t* x/j #find the next term
        sum=sum+t; #add it to sum
        print('iteration= %d\tsum= %f' %(j+1,sum))
        
    