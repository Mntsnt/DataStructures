from queue import LifoQueue

stack = LifoQueue()

# Push elements
stack.put(10)
stack.put(20)
stack.put(30)

# Pop element
top_element = stack.get()
print("Popped element:", top_element)  # Output: 30

# Check if stack is empty
print("Stack is empty:", stack.empty())