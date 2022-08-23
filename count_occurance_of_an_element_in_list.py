# 22-7-22
# count occurrences of an element in a list
def countX(lst, x):
    return lst.count(x)


# driver code
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 10, 20, 20, 30, 40]
x = 30
print('{} has occurred {} times'.format(x, countX(lst, x)))



