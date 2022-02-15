#11-2-22
#retrieving employee details from a list
emp=[]

n=int(input('How many employee? ')) # accept input into n

for i in range(n): #repeat for n times
    print('Enter id: ',end='')
    emp.append(int(input()))
    print('Enter name: ',end='')
    emp.append(input())
    print('Enter Salary: ',end='')
    emp.append(float(input()))
    
print('the list is created with employee data. ')

id=int(input('Enter employee  id: '))

#display employee details upon talking id .
for i in range(len(emp)):
    if id==emp[i]:
        print('id= {:d},Name= {:s}, Salary={:.2f}'.format(emp[i],emp[i+1],emp[i+2]))
        break
               
    