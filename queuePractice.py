from queue import Queue

# Create a queue
q = Queue()

# Enqueue elements
q.put(10)
q.put(20)
q.put(30)

print("Queue size:", q.qsize())

# Dequeue elements
while not q.empty():
    item = q.get()
    print("Dequeued:", item)

print("Queue is empty:", q.empty())