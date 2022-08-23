#26-3-22
#program to evaluate sine series
#accept user input
x,n=[int(i)  for i in input("enter angle value, no. of iterations: ").split(',')]
#convert the angle from degrees into radians
r=(x*3.14159)/180
#this become the first term
t=r
#till now,find the sum
sum=r
#display the iteration number and sum
print('Iteration=%d\tsum=%f'%(1,sum))
#denominator for the second term
i=2
#repeat for 2nd to nth terms
for j in range(2,n+1):
        t=(-1)*t*r*r/(i*(i+1))#find the next term
        sum=sum+t; #add it to sum
        print('iteration= %d\tsum= %f' %(j,sum))
        i+=2 #increaase i value by 2 for denominator for next term
    

