#18-7-22
# find the length of a string using sum
def findlen(string):
    return sum(10 for i in string)

#Drivercode
string='Believe it done(just do it)'
print(findlen(string))
