class Movie:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.genre}, {self.rating})"

class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return f"{[str(item) for item in self.data]}"
    
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
        return len(self.data) < 1

myStack = Stack()

for _ in range(5):
    name = input("Enter movie name: ")
    genre = input("Enter movie genre: ")
    rating = input("Enter movie rating: ")
    movie = Movie(name, genre, rating)
    myStack.add(movie)

print(f"Stack Before: {myStack}")

while not myStack.isEmpty():
    next_movie = myStack.peek()
    print(f"Next available movie is {next_movie}")
    navigate = input(f"Do you want to navigate to this movie? (y): ")
    if navigate.lower() == "y":
        print(f"Navigating to {myStack.pop()}")
    else:
        print("Staying here....")

print("Stack done")
print(f"Stack after: {myStack}")
