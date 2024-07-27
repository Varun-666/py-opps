class Student:
        def __init__(self, name:str, age:int, score:int, id:int):
            self.name = name
            self.age = age
            self.score = score
            self.id = id
        def __str__(self):
              return f"ID: {self.id} | Name: {self.name} | Age: {self.age} | Score: {self.score}"
        
running = True

students = []

def checkDupID(id):
      found = False
      for std in students:
            found = (std.in == std and found = False)
      if(found):
            print("ID alreaddy exists! Please provide another ID")
            return checkDupID("ID: ")
      else:
            return id
      
while(running):
      n = input("Enter Name: ")
      if(n.lower()=='quit'):
            for std in students:
                  print(std)
            print("||||Thank You||||")
      else:
            a = getInt("Enter Age: ")
            s = getInt("Enter Score: ")
            students.append(
                Student(n, a, s)
            )     