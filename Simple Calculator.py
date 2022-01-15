# Python Make a simple calculator

# This function add two number
def add(x,y):
    return  x+y

# This function Subtract two number
def Subtract(x,y):
    return  x-y

# This function Multiply two number
def Multiply(x,y):
    return  x*y

# This function Divide two number
def Divide(x,y):
    return  x/y    
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):


        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")