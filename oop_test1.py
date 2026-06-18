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