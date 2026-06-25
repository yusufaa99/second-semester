# this project is implemented with respect to pholimorphism understanding

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def reverse(self):
        pass
    @abstractmethod
    def horn(self):
        pass
    
    def park(self):
        return "Parked"

    @property
    @abstractmethod
    def color(self):
        pass

class Toyota(Car):

    def drive(self):
        return "Driving Toyota"
    
    def reverse(self):
        return "Reversing Toyota"

    def horn(self):
        return "Beem Beem"
    
    @property
    def color(self):
        return "Black"

car1 = Toyota()

print(car1.drive())
print(car1.horn())
print(car1.reverse())
print(car1.park())
print(car1.color)

