class Shape:
    def __init__(self):
        self.color=None
        self.weight=None

    def get(self,i):
        return self.data[i]

    def square(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color='blue'):
        super().__init__(color)
        self.color = 'blue'
        self.radius=radius
    def square(self):
        print('in circle')
        return 3.14*self.radius**2

class Rectangle(Shape):
    def __init__(self, a, color='blue'):
        super().__init__(color)
        self.a = a
    def square(self):
        return self.a**2



circle = Circle(4)
circle.color='red'
circle.weight=10
print(circle.square())
circle.get(2)

rect=Rectangle(2)
print(rect.square())