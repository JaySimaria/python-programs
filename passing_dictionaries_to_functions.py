# a function that takes a dictionary as parameter
def fun(dictionary):
    for i,j in dictionary.items():
        print(i, '--',j)
#take a dictionary
d={'a':'apple','b':'Book','c':'Cook'}

#call the functions and pass the dictionary
fun(d)