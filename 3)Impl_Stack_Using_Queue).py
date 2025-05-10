from collections import deque

class StackUsingDeque:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "Stack is Empty"
        return self.queue.popleft()

    def peek(self):
        if len(self.queue) == 0:
            return "Stack is Empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# === Driver Code ===
if __name__ == "__main__":
    stack = StackUsingDeque()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element:", stack.peek())  # Output: 30
    print("Stack size:", stack.size())   # Output: 3

    print("Popped:", stack.pop())        # Output: 30
    print("Top after pop:", stack.peek())# Output: 20
    print("Is stack empty?", stack.is_empty())  # Output: False

    stack.pop()
    stack.pop()
    print("Popped again:", stack.pop())  # Output: Stack is Empty
