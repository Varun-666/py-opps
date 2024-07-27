class vehicle:

    def __init__(self,wheels):
        self.wheels = wheels

    def type(self):
        return self.wheels+ "wheeler vehicle"
    
    def sound():
        return "Honk Honk"
    
class car(vehicle):

    def __init__(self, colour, brand):
        super().__init__(4)
        self.colour = colour
        self.brand = brand

    def sound():
        return "Bomp Bomp"
    
class bike(vehicle):

    def __init__(self, colour, brand):
        super().__init__(2)
        self.colour = colour
        self.brand = brand

    def sound():
        return "Beep Beep"
    
class truck(vehicle):

    def __init__(self, colour, brand):
        super().__init__(8)
        self.colour = colour
        self.brand = brand

a1 = car("red", "Skoda")
a2 = truck("green", "Tata")
a3 = bike("blue", "Yamaha")

# print(a1.type()+"makes sound"+a2.sound())