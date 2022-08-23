# 11-2-22

#take two lists
scholar1=['Jalpa','Jay','Vikas','Yash','Sarthi']
scholar2=['Mayur','Rushit','Jalpa','Jay']

#convert them into sets
s1=set(scholar1)
s2=set(scholar2)

#find intersection of two sets
s3=s1.intersection(s2)

#convert the resultant of two sets
common = list(s3)
#display the list
print(common)