from abc import ABC, abstractmethod
from enum import Enum
class Dog:
    sound = "wooh wooh wooh"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} Year old"


dog1 = Dog("bush", 5)
dog2 = Dog("puppy", 2)

print(dog1)
print(dog2)


class animal:
    def __init__(self,name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound
    
    def sound1(self, sound1):
        self.sound1 = sound1
        return f"sound is {self.sound1}"
    
    def prints(self):
        print(f"Name is {self.name}", f"Color is {self.color}", f"and sound is {self.sound}")

dog = animal("bush", "black", "wooh wooh")
dog.prints()
cat = animal("mussy", "white", "meo meo")
cat.prints()
print(cat.sound1('mooeo meeo'))



class A:
    def __new__(cls):
        return "new instance created"
    
    def __init__(self):
        print("initializing the object")

print(A())



class Calculator:
    def add(self, a, b, c=None, d=None):
        if d is not None:
            return a + b + c + d
        elif c is not None:
            return a + b + c
        else:
            return a + b
        
    def mult(self, a=1, b=1, *args):
        result = a*b

        for num in args:
            result *= num

        return result
    

# creating the object of the calculator
calc = Calculator()
# with default
print(calc.mult())
print(calc.mult(5))

#  with parameters
print(calc.mult(5,4))
print(calc.mult(2,5,6,10))


print(calc.add(2,4))
print(calc.add(2,4,8))
print(calc.add(2,4,5,7))


s = "GFG"
it = iter(s)

# print(next(it))
# print(next(it))
# print(next(it))

# enum implementation
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SARTUDAY = 6
    SUNDAY = 7

def current_day(day):

    if day == Day.MONDAY:
        print(f"Today is: {Day.MONDAY.name}")

current_day(Day.MONDAY)

# custom iteration implementation
class Even_num:
    def __init__(self, limit):
        self.limit = limit
        self.n = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.limit:
            raise StopIteration
        
        x = self.n
        self.n += 2
        return x

even = Even_num(20)

for num in even:
    print(num)


lst = [10,20,30,40,50,60,70,80,90,100]
it = iter(lst)

print("\nList iteration\n")
while True:
    try:
        print(next(it))
    except StopIteration:
        print('End of thr iteration')
        break




class Validator:
    @abstractmethod
    def validate():
        pass

    @abstractmethod
    def get_validate():
        pass

class NameValidator(Validator):
    def validate(self):
        return "Name validator"
    
    def get_validate(self):
        return "Get Name Validator"

class AgeValidator(Validator):
    def validate(self):
        return "Age validator"
    
    def get_validate(self):
        return "Get Age Validator"

validator = NameValidator()
value = validator.validate()
print(value)
# def validate(name):
#     clean = name.strip()
#     if not clean:
#         return False, None
    
# name = "     muhammad sani yunus     "
# print(validate(name))

class Account(ABC):
    @abstractmethod
    def deposite():
        pass

    @abstractmethod
    def withdraw():
        pass

    @abstractmethod
    def balance():
        pass

    @abstractmethod
    def info():
        pass

class Jaiz(Account):
    def __init__(self, name, acc_no):
        self.__name = name
        self.acc_no = acc_no

    def deposite(self):
        pass

    def withdraw(self):
        pass

    def balance(self):
        pass

    def info(self):
        print(f"Name: {self.__name}, Account: {self.acc_no}")
    
         
if __name__ == "__main__":
    jaiz = Jaiz("Khalid", "2121000012")
    jaiz.info()


class Student:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        x3 = Student(x1, y1)
        return x3

if __name__ == "__main__":
    std1 = Student(20, 25)
    std2 = Student(10, 30)
    std3 = std1 + std2
    print(std3.x, std3.y)