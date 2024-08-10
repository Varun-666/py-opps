class person:
    name = "no Name set"
    def setName(self,n):
        self.name = n

    def __str__(self):
        return "This is a person named: " + self.name

    def __repr__(self):
        return "This is : " + self.name

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class professional(person):
    __key = 'secret key123'

    def __init__(self, name, age, greet):
        self.greet = greet
        self.age = age
        self.name = name
    def greet(self):
        print(self.greet)
    def __del__(self):
        print(self.name+ "deleted!")
    def gerKey(self):
        return self.__key
    
p1 = person("Jaxx")
p2 = person("John")
p3 = professional("Tom")
p1.score = 99

# print(p1)
# print(p2)
# print(p3)

class Car:
    colour = "no colour"
    def setColour(self, c):
        self.colour = c
    def __str__(self):
        return "The colour of car is: " + self.colour
    def __init__(self, colour):
        self.colour = colour

class Brand(Car):
    pass

c1 = Brand("Red")
# print(c1)

