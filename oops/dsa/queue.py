class Queue:
    def __init__(self):
        self.q = []
        print("Empty Queue Created!!")

    def __str__(self):
        return f"{self.q}"
    
    def enque(self, item):
        self.q.append(item)
        print(f"Item {item} has been enqued.")

    def deque(self):
        return self.q.pop(0)

    def skip(self):
        self.q.pop(0)

    def peek(self):
        return self.q[0]
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def size(self):
        return len(self.q)