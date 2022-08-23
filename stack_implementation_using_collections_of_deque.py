# 17-8-22
# stack implementation using collections of deque
from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('j')
stack.append('s')
stack.append('r')

print('Initial stack:')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)



