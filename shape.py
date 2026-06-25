class shape:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"{self.identity()}"
    
    def identity(self):
        return f"shape"
    
    def area(self):
        return f"Area of {self.identity()}: {self.length*self.width} Length = {self.length} Width = {self.width}"

class rectangle(shape):
    def identity(self):
        return f"Rectangle"

class  square(shape):

    def identity(self):
        return f"square"

class triangle(shape):
    def __init__(self, length, width, heigth):
        super().__init__(length, width)
        self.heigth = heigth
    
    def area(self):
        return f"Area of {self.identity()}: {self.heigth*self.width*self.heigth} Length = {self.length} Width = {self.width} Height = {self.heigth}"

    def identity(self):
        return f"Triangle"
    
rect = rectangle(50,20)
print(rect.area())
# print(rect.identity())

sqr = square(20,20)
print(sqr.area())
# print(sqr.identity())

tri = triangle(10,20,30)
print(tri.area())
