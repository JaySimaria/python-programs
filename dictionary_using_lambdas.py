#sorting a dictionary  by key or value
#take a dictionary
colors={10:"red",40: "green",15:"blue",25:"White"}
#sort the dictionary the keys , i.e. 0th element
c1=sorted(colors.items(),key=lambda t: t[0])
print(c1)

#sort the dictionary by values ,i.e. list element
c2=sorted(colors.items(),key=lambda t: t[1])
print(c2)