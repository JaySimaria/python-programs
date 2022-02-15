#displaying list elements in reverse order
days=['Sunday','Monday','Tuesday','Wednesday','Thursday']

print('\nIn reverse order: ')
i=len(days)-1 # i will be 4
while i>=0:
    print(days[i]) #display from  4th to 0th elements
    i-=1
    
print('\nIn reverse order: ')
i=-1 #days [-1] represents lasst element
while i>=-len(days): #display from -1th to -5th elements
    print(days[i])
    i-=1