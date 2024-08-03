class Movie:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.genre}, {self.rating})"
    
class Queue:
    def __init__(self):
        self.q = []

    def __str__(self):
        return f"{[str(item) for item in self.q]}"
    
    def enque(self, item):
        self.q.append(item)
        print(f"Item {item} has been enqueued.")

    def deque(self):
        if not self.isEmpty():
            return self.q.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")
    
    def peek(self):
        if not self.isEmpty():
            return self.q[0]
        else:
            print("Queue is empty. Cannot peek.")
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def size(self):
        return len(self.q)
    
myQueue = Queue()

i = int(input("How many movies do you want to add: "))

for _ in range(i):
    name = input("Enter movie name: ")
    genre = input("Enter movie genre: ")
    rating = input("Enter movie rating: ")
    try:
        rating = float(rating)
    except ValueError:
        print("Invalid rating. Please enter a number.")
        continue
    movie = Movie(name, genre, rating)
    myQueue.enque(movie)

print(f"Queue Before: {myQueue}")
print(f"Queue Now: {myQueue}")

while not myQueue.isEmpty():
    next_movie = myQueue.peek()
    print(f"Next available movie is {next_movie}")
    navigate = input(f"Do you want to navigate to this movie? (y/n): ")
    if navigate.lower() == "y":
        print(f"Navigating to {myQueue.deque()}")
    else:
        myQueue.deque()
        print("Staying here....")

print("Queue done")
print(f"Queue after: {myQueue}")
