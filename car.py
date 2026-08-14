class Car:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model
    
    def drive(self):
        print(f"{self.name} is Driving")
    
    def reverse(self):
        print(f"{self.name} is reverse")

class Toyota(Car):
    def __init__(self, name, color, model, areal):
        super().__init__(name, color, model)
        self.areal = areal

        
        print(f"{self.areal}")

    def nitro(self):
        print(f"{self.name} has a Nitro")

class Honda(Car):
    pass

Toyota = Toyota("Toyota", "Black", "Camry 2020", True)
Toyota.drive()
Toyota.reverse()
print(Toyota.name)
Toyota.nitro()

honda = Honda("Honda", "White", "Accord 2013")
honda.drive()
honda.reverse()

