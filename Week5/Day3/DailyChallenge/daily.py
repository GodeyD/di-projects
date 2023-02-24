import math

class Circle:

    def __init__(self, radius: int) -> None:
        self.radius = radius # 4
        self.diameter = radius * 2 # 8

    @classmethod
    def from_diameter(cls, diameter: int):
        return Circle(diameter//2) 
    def __str__(self):
        return f'Radius: {self.radius}, Diameter: {self.diameter}, Area: {self.area():.3f}'

    def area(self):
        return math.pi * self.radius ** 2

    def __add__(self, other_circle):
        result = Circle(self.radius + other_circle.radius)
        return result
 
    def __gt__(self, other_circle) -> bool: 
        return self.area() > other_circle.area()

    def __eq__(self, other_circle) -> bool:
        return self.area() == other_circle.area()

circle1 = Circle(2)

print(circle1)

circle2 = Circle.from_diameter(8)
circle3 = circle1 + circle2
print(circle3)
print(circle1 > circle2)
print(circle1 == circle2)
circles = [circle3, circle1, circle2]
circles.sort()