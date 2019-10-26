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
