#Ex1----------------------------------------------------------------------------------------------------------------
import math

class Device:
    def __init__(self, color):
        self.color=color


class CoffeeMachine(Device):
    def __init__(self, color, pressure, grain_tank_volume):
        super().__init__(color)
        self.pressure = pressure
        self.grain_tank_volume = grain_tank_volume
    
    def making_coffee(self):
        return "The coffee machine makes coffee"
        
    
class Blender(Device):
    def __init__(self, color, power, volume):
        super().__init__(color)
        self.power = power
        self.volume = volume
        
    def blending(self):
        return "blender is blending"
    
class MeatGrinder(Device):
    def __init__(self, color, power, efficiency):
        super().__init__(color)
        self.power = power
        self.volume = efficiency
    def grind_meat(self):
        return "MeatGrinder grinding meat"
        


#Ex2----------------------------------------------------------------------------------------------------------------



class Ship:
    def __init__(self, color, capacity):
        self.color=color


class Frigate(Ship):
    def __init__(self, color, capacity, number_of_masts):
        super().__init__(color, capacity)
        self.number_of_masts=number_of_masts
    
    def sailing(self):
        return "Frigate sailing at a speed of 55 km/h"
        
    
class Destroyer(Ship):
    def __init__(self, color, capacity, speed):
        super().__init__(color, capacity)
        self.speed=speed
       
    def anti_submarine_warfare(self):
        return "Destroyer fighting submarines."


class Cruiser(Ship):
    def __init__(self, color, capacity, armament):
        super().__init__(color, capacity)
        self.armament=armament

    def setting_up_minefields(self):
        return "Cruiser setting up minefields"


#Ex3----------------------------------------------------------------------------------------------------------------
    

class Square:
    def __init__(self, color, a, b):
        self.color=color
        self.a=a
        self.b=b
    def greeting(self):
        return "Hello! I am Square"
class Circle:
    def __init__(self, color, radius):
        self.color=color
        self.radius=radius
    def greeting(self):
        return "Hello! I am Circle"
    
class CircleInSquare(Square, Circle):
    def greeting(self):
        return "Hello! I am Circle in Square"
    

#Ex4----------------------------------------------------------------------------------------------------------------



class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def spin(self):
        return "The wheels are spinning"


class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        return "Engine started"


class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def open(self):
        return"Doors are open"

    def close(self):
        return"Doors are closed"


class Car(Wheels, Engine, Doors):
    def __init__(self, number_of_wheels, power, number_of_doors, name, color):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, power)
        Doors.__init__(self, number_of_doors)

        self.name = name
        self.color = color

    def drive(self):
        return "car is driving"

#Ex5----------------------------------------------------------------------------------------------------------------


class Shape():
    def __init__(self, data=None):
        self.data = data
    
    def Show(self):
        print(self.data)

    def Save(self, filename = "shape.txt"):
        with open(filename, "r") as f:
            old_data= f.read()

        with open(filename, "w") as f:
                f.write(old_data + "\n" + f"{self.data}")

    def Load(self, filename = "shape.txt"):
        with open(filename, "r") as f:
            self.data = f.read()

class Square(Shape):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        data = {
            "x" : self.x,
            "y" : self.y,
            "size" : self.size,
        }
        
        super().__init__(data)


class Rectangle(Shape):
    def __init__(self, x, y, size_a, size_b):
        self.x = x
        self.y = y
        self.size_a = size_a
        self.size_b = size_b


        data = {
            "x" : self.x,
            "y" : self.y,
            "size_a" : self.size_a,
            "size_b" : self.size_b,
        }
        
        super().__init__(data)


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


        data = {
            "x" : self.x,
            "y" : self.y,
            "radius" : self.radius,
        }
          
        super().__init__(data)


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        data = {
            "x" : self.x,
            "y" : self.y,
            "width" : self.width,
            "height" : self.height,
        }
        
        super().__init__(data) 


shape=Shape()
        

sqruare = Square(10, 5, 8)
sqruare.Show()
sqruare.Save()



rectangle = Rectangle(10, 5, 10, 5)
rectangle.Show()
rectangle.Save()



circle = Circle(3, 10, 10)
circle.Show()
circle.Save()


ellipse = Ellipse(10, 5, 50, 10)
ellipse.Show()
ellipse.Save()

with open("shape.txt", "r") as f:
            data= f.read()
            result_list=data.split('\n')
print(result_list)


