#dictionary methods
#create a dictionary with employee details.
dict={'Name': 'Jay', 'Id':200,'Salary':9080.50}

#print entire dictionary
print(dict)

#display only keys
print('keys in dict= ',dict.keys())

#display only values
print('Values in dict= ',dict.values())

#display both key and value pairs on tuples
print('Items in dict= ',dict.items())

#program to find sum of values in a dictionary
#enter the dictionary entries from keybord
dict=eval(input("enter elements in {}: "))

# find the sum of values
s=sum(dict.values())
print('sum of values in the dictionary: ',s) # display sum


#creating a dictionary from the keyboard
x={} #take an empty dictionary

print('How many elements? ',end='')
n=int(input()) #n indicates no. of key-value pairs

for i in range(n): #repeat for n times
    print('Enter key: ',end='')
    k=input() #key is string
    print('Enter its value: ',end='')
    v=int(input()) #value is integer
    x.update({k:v}) # store the key-value pair in dictionary x
    
# display the dictionary
print('The dictionary is: ', x)

#creating a dictionary with cricket players names and scores
x={} #take an empty dictionary

print('How many players? ',end='')
n=int(input()) #n indicates no. of key-value pairs

for i in range(n): #repeat for n times
    print('Enter player name: ',end='')
    k=input() #key is string
    print('Enter runs: ',end='')
    v=int(input()) #value is integer
    x.update({k:v})
    
#display only players names
    print('\nPlayers in this match: ')
    for pname in x.keys(): #keys() will give only keys
        print(pname)
        
# accept a player name from keyboard
print('Enter player name: ',end=' ')
name=input()

#find the runs done by the players
runs=x.get(name,-1)
if(runs== -1):
    print('player not found')
else:
    print('{} made runs {}.'.format(name,runs))
        
    

    
