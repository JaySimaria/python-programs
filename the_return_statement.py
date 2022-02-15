#26-3-22
#a function to find sum of two numbers
def sum(a,b):
    print('sum= ',a+b)
sum(6,12) #call sum() and pass 5 to 10
sum(1.5,2.5)#call sum() and pass 1.5 and 2.5


# a function to return sum of the two numbers
def sum (a,b):
    return a+b # result is returned from here
#call sum() and pass 5 and 10
#get the returned result into res
res=sum(12,20)
print('The result is ',res)


#Program to print prime numbers upto a given numbers
#accept upto what numbers the user wants\
max = int(input("upto what numbers?"))

for num in range(3,max+1): #generate from 2 onwards till max
    for i in range(3,num): # i represents numbers from 2 to num-1
        if(num %i)==0: # if num is divisible by i
            break # it is not prime, hence go back and check next num
    else:
        print(num)# otherwise it is prime and hence display




