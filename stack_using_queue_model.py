## Implementing stack using the queue module
from queue import LifoQueue

# Implementing stack using the queue module
from queue import LifoQueue

# Initializing a my_stack stack with maxsize
my_stack = LifoQueue(maxsize = 5)

# qsize() display the number of elements
# in the my_stack
print(my_stack.qsize())

# put() function is used to push
# element in the my_stack
my_stack.put('x')
my_stack.put('y')
my_stack.put('z')

print("Stack is Full: ", my_stack.full())
print("Size of Stack: ", my_stack.qsize())

# To pop the element we used get() function
# from my_stack in
# LIFO order
print('\nElements poped from the my_stack')
print(my_stack.get())
print(my_stack.get())
print(my_stack.get())

print("\nStack is Empty: ", my_stack.empty())
