class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Cannot pop, stack is empty"
        return self.items.pop()

    def top(self):
        if len(self.items) == 0:
            return "Cannot top, stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Using the stack
stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(f"Stack content = {stack}")
print(f"Popped item = {stack.pop()}")
print(f"Stack content = {stack}")
print(f"Top item after pop = {stack.top()}")
print(f"Stack is empty = {stack.is_empty()}")
