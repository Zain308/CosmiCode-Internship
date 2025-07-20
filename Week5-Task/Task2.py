class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == "__main__":
    # Example usage
    rect = Rectangle(5, 3)
    print(f"Rectangle Area: {rect.area():.2f}")
    print(f"Rectangle Perimeter: {rect.perimeter():.2f}")
    
    circle = Circle(4)
    print(f"Circle Area: {circle.area():.2f}")
    print(f"Circle Perimeter: {circle.perimeter():.2f}")
    
    triangle = Triangle(3, 4, 5)
    print(f"Triangle Area: {triangle.area():.2f}")
    print(f"Triangle Perimeter: {triangle.perimeter():.2f}")