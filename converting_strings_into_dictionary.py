#converting a string into a dictionary
#take a string
str="Vijay=23,Ganesh=20,lakshmi=19,Nikhil=22"

#brake the string at ',' and then at '='
#store the pieces into a list lst
lst=[]
for x in str.split(','):
    y= x.split('=')
    lst.append(y)
# convert the list into dictionary 'd'
#but this'd' will have both name and age as as strings
d=dict(lst)

#create a new dictionary 'd1' with name as string
#and age as integer
d1={}
for k,v in d.items():
    d1[k] = int(v)
#display the final dictionary
print(d1)