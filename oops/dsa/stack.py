class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return f"{self.data}"
    
    def add(self, item):
        self.data.append(item)
    
    def peek(self):
        if not self.data:
            return None
        return self.data[-1]
    
    def pop(self):
        if not self.data:
            return None
        return self.data.pop()

myStack = Stack()

myStack.add("test")
myStack.add("good")
myStack.add("Happy")

print(f"Stack Before: {myStack}")

print(f"The next item in stack is {myStack.peek()}")
myStack.pop()

print(f"Stack after: {myStack}")
