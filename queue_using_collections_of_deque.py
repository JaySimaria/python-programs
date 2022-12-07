# 6-12-22
#queue using collections of deque
from collections import deque
#creating empty deque
queue = deque()
# adding element to the queue
queue.append('a')
queue.append('b')
queue.append('c')


print("initial queue")
print(queue)

# popleft the element into the queue by using FIFO
print("\nElements dequeued from the queue")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("\nQueue after removing elements")
print(queue)