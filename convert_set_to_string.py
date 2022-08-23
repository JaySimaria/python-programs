#13-7-22
#convert set to string
# create a set
s = {'a', 'b', 'c', 'd'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)

# convert Set to String
S = ', '.join(s)
print("The datatype of s : " + str(type(S)))
print("Contents of s : ", S)
