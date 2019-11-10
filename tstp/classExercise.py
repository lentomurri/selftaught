import math

class Orange: 
    # standard initial def, always start with this one 
    def __init__(self):
        self.weight
        self.color
        print("Created!")
    # you can create all the methods you want for the instances

class Apple:
    def __init__(self, s, c, w, t ):
        self.shape = s
        self.color = c
        self.weight = w
        self.taste = t
    def eatApple(self):
        print("Eaten it all!")
        

def createApple():
    shape = input("Enter the shape: ")
    color = input("Enter the color: ")
    try:
        weight = int(input("Enter the weight: "))
    except ValueError:
        input("Please enter only numeric values")
        weight = int(input("Enter the weight: "))
    taste = input("Enter the taste: ")
    apple = Apple(shape, color, weight, taste)
    return apple

class Circle():
    def __init__(self, r, d):
        self.ray = r
        self.diameter = d
    def area(self):
        areaResult = math.pi * math.pow(self.ray, 2)
        print(areaResult)

class Triangle():
    def __init__(self, s, h):
        self.side = s
        self.height = h
    def area(self):
        print((self.side * self.height) / 2)


class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
    def calculate_perimeter(self):
        list_sides = [self.side1, self.side2, self.side3, self.side4, self.side5, self.side6]
        print(sum(list_sides))

class Rectangle():
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def calculate_perimeter(self):
        result = (self.width * 2) + (self.height * 2)
        return result
class Shape():
    def _init__(self):
        pass
    
    def what_am_I(self):
        print("I am a shape")
class Square(Shape):
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)
    
    def calculate_perimeter(self):
        result = self.side * 4 
        if result <= 0:
            print("The Square has been flattened into the Upside Down")
        else:
            return result
    
    def change_side(self):
        num = int(input("Enter a positive or negative number to increase or decrease the side: "))
        self.side = self.side + (num)
    
    def __str__(self):
        return ((str(self.side) + " by ") * 3 + str(self.side))
        
square1 = Square(4)
print(square1) 
class Horse():
    def __init__(self, race, age, owner):
        self.race = race
        self.age = age
        self.owner = owner

class Owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age




