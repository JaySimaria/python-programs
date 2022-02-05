#5-2-22
def display(lst):
    """ to display the strings """
    for i in lst:
        print(i)
print('enter strings separted by comma: ')
lst=[x for x in input().split(',')]
display(lst)