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
