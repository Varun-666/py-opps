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
    
class Car:
    def __init__(self, make , color, model):
        self.make = make
        self.color = color
        self.model = model
    def __str__(self):
        return self.make

myQ = Queue()

for x in range(5):
    myQ.enque(
    Car(input("Enter Make of the car: "),
    input("Enter Color of the car: "),
    input("Enter Model of the car: "))
)
    
while(not myQ.isEmpty()):
    print("===============")
    print("1 - print que")
    print("2 - peek next")
    print("3 - deque next")
    print("4 - skip next")

    inp = int(input("Enter Option: "))

    if(inp==1):
        print(myQ)
    elif(inp==2):
        print(f"next car is a {myQ.peek()}")
    elif(inp==3):
        Car = myQ.deque()
    elif(inp==4):
        print(f"Skiping")
    