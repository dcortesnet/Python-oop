class Polygon:
    def __init__(self, width, height):
        self.name = 'Polygon'
        self.width = width
        self.height = height

    @property
    def polygon_type(self):
        return f"The polygon type is {self.name}"

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.name = 'Rectangle'

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 10)

print(rectangle.area)           # 50
print(rectangle.polygon_type)   # The polygon type is Rectangle