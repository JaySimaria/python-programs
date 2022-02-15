#sorting a tuple that contains tuple as element
emp=((10,"Jay",15000),(20,"Rushit",8000),(30,"Mayur",10000),(40,"Jalpa",12000))

print(sorted(emp))
print(sorted(emp,reverse=True)) # sorts by default on id
print(sorted(emp,key=lambda x: x[1])) # sort on name
print(sorted(emp,key=lambda x: x[2])) #sort on salary


