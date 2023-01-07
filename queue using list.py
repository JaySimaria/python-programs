# 6-12-22
# queue using list
# create a empty queue
queue = []
#  Adding elements to the queue
queue.append('b')
queue.append('j')
queue.append('s')
queue.append('a')
queue.append('r')

print("initialqueue")
print(queue)

# pop the element into the queue by using FIFO'
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)