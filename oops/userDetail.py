class Student:
    def __init__(self, name: str, age: int, score: int, id: int):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Age: {self.age} | Score: {self.score}"

class DuplicateError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def get_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def check_dup_id(id: int, students: list) -> bool:
    for std in students:
        if std.id == id:
            return True
    return False

students = []
running = True

while running:
    n = input("Enter Name: ")
    if n.lower() == 'quit':
        running = False
    else:
        a = get_int("Enter Age: ")
        s = get_int("Enter Score: ")

        while True:
            id = get_int("Enter ID: ")
            if not check_dup_id(id, students):
                students.append(Student(n, a, s, id))
                break
            else:
                print("ID already exists! Please enter another ID.")

# Print all student information
print("|||| Students Information ||||")
for std in students:
    print(std)
print("|||| Thank You ||||")
