#find sum of even numbers
import sys
#read command line arguments except the program name
args=sys.argv[1:]
print(args)
sum=0
#find sum of even arguments
for a in args:
    x=int(a)
    if x%2==0:
        sum+=x
print('sum of events=',sum)        