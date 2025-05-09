class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self):
        self.items.append(items)
    def dequeue(self):
        if len(self.items)==0:
            return "Cannot pop,stack empty"
        x=self.items.pop()
        return x
    def front(self):
        if len(self.items)==0:
            return "Cannot pop,stack empty"
        return self.items[0]
    def rear(self):
        if len(self.items)==0:
            return "Cannot pop,stack empty"
        return self.items[-1]
stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(f"Stack content = {stack}")
print(f"Popped item = {stack.pop()}")
print(f"Stack content = {stack}")
print(f"Top item after pop = {stack.top()}")
print(f"Stack is empty = {stack.is_empty()}")
    

        
