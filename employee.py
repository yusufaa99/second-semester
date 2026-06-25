# this project is implemented with respect to pholimorphism understanding

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working 8am-6pm"
    
    def bonus(self):
        return self.salary*0.05
    
    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}"
    
class Manager(Employee):
    
    def bonus(self):
        return self.salary * 0.15
    
    def work(self):
        return f"{self.name} Manages all the organisation and he also attend meating"
    
    def Planning(self):
        return f"{self.name} Setting specific goals, defining strategies, and mapping out the exact steps required to reach organizational targets"

class Developer(Employee):
    def __init__(self, name, salary, programming_lang):
        super().__init__(name, salary)
        self.programming_lang = programming_lang

    def work(self):
        return f"{self.name} is {self.programming_lang} Software developer"
    
    def debugging(self):
        return f"{self.name} always debug code"
    

    def bonus(self):
        base_bonus = super().bonus()
        
        extra = 1000 if self.programming_lang in ["java", "python", "c", "c++"] else 0

        return base_bonus + extra
        
employees = [
    Employee("Muhammad Sani", 20000),
    Manager("Hamza Abubakar", 50000),
    Developer("Abubakar Ibarahima", 40000, "python"),
    Developer("suleiman Muhammad", 38000, "java")
]

for emp in employees:
    print(f"\n{emp}")
    print(f"work: {emp.work()}")
    print(f"Bonus: ${emp.bonus():.2f}")

    if isinstance(emp, Developer):
        print(f"Debugging: {emp.debugging()}")
    
    elif isinstance(emp, Manager):
        print(f"Planning: {emp.Planning()}")
