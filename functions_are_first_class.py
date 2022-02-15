# function defined
def multiply_num(a):
    b = 40
    r = a*b
    return r
 
 
# drivercode
# assigning function
z = multiply_num
 
# invoke function
print(z(6))
print(z(10))
print(z(100))


def display(str):
    return 'hai '+str
x=display("krishna")
print(x)


def display(str):
    def message():
        return'How are U?'
    result=message()+str
    return result
print(display("Krishna"))


def display(fun):
    return 'Hai'+fun
def message():
    return'How are U?'
print(display(message()))


def display():
    def message():
        return 'How are U?'
    return message
fun=display()
print(fun())
