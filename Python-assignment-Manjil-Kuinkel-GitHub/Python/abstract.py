from shape import Shape

class Square(Shape):
    def __init__(self):
        self.length=3
        self.bredth=4

    def area(self):
        return(self.length*self.bredth)
    
s=Square()
print(s.area())

s.display()