#using for loop with dictionaries
#take a dictionary
colors={'r':"red",'g':"green",'b':"blue",'w': "white"}

# display only keys
for k in colors:
    print(k)
    
#pass keys to dictionary and display the values
    for k in colors:
        print(colors[k])
        
# items() method returns key and value pair into k,v
for k,v in colors.items():
    print('keys={} Value={}'.format(k,v))
    
    
#finding how many times each letter is repeated in a string
#take a string with some letters
str="Book"

#take an empty dictionary
dict={}

#store into dict each letter as key and its
#number of coccurences as value
for x in str:
    dict[x]= dict.get(x,0) +1
    
#display key and value parts of dict
    for x,v in dict.items():
        print('key= {}\t Its occurence={}'.format(k,v))

