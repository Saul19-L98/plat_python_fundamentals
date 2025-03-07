class Calculator:    
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

Counter.increment()
Counter.increment()
print(Counter.count)

class Circle:
    def __init__(self,radius:float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.1416 * (self._radius ** 2)

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self,value:float):
        if value < 0:
            raise ValueError("The radius can not be a negative value.")
        self._radius = value
    
circle = Circle(5)
print(circle.area)
circle.radius = 10
print(circle.area)