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
    def isEmpty(self):
        return len(self.data)<1

myStack = Stack()

myStack.add(input("Enter site name: "))
myStack.add(input("Enter site name: "))
myStack.add(input("Enter site name: "))
myStack.add(input("Enter site name: "))
myStack.add(input("Enter site name: "))

print(f"Stack Before: {myStack}")

while(not myStack.isEmpty()):
    print(f"Next available item is {myStack.peek()}")
    item_vale = input(f"Do you want to navigate there? ")
    if(item_vale=="y"):
        print(f"Navigating to {myStack.pop()}")
    else:
        print("Staying here....")
print("Stack done")
print(f"Stack after: {myStack}")