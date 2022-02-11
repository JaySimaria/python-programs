#5-2-22
def calculate(lst):
    """ to find total and average """
    n=len(lst)
    sum=0
    for i in lst:
        sum+=i
        avg=sum/n
        return sum,avg
print('enter numbers separted by space: ')
lst=[int(x) for x in input().split()]
x,y=calculate(lst)
print('total: ',x)
print('average: ',y)

def display(lst):
    """ to display the strings """
    for i in lst:
        print(i)
print('enter strings separted by comma: ')
lst=[x for x in input().split(',')]
display(lst)