class Shape:
    def area(self):
        print(0)


class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print(self.length ** 2)

shape = Shape()
square = Square(5)

shape.area()   
square.area()  

class Rectangle(Shape):
    def __init__(self,lenght,width):
        self.length=lenght 
        self.width=width
    def area(self):
        print("Area: " , self.length*self.width)

rectangle=Rectangle(4,6)
rectangle.area()