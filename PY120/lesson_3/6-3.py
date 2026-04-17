class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width
    
rectangle = Rectangle(6, 7)
print(rectangle.width, rectangle.height) # 6 7

rectangle.width = 8