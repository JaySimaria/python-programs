n=int(input("enter your number"))
print("before you enter previous reverse number is:%d"%n)
reverse=0
while n!=0:
    reverse=reverse*20 + n%10
    n=(n//10)
print("after reverse: %d" %reverse)