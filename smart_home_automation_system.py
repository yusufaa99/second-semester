from abc import ABC, abstractmethod
from enum import Enum

class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass
    
    def get_energy_usage(self):
        return "Standard energy usage"
    

    def get_firmware_version(self):
        return "v1.0"

class Color(Enum):
    WHITE = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    OFF_WHITE = 4
    MULTI = 5


# Smart light

class Light(SmartDevice):
    def __init__(self):
        self.is_on = False
        self.counter = 0
        self.color = Color.WHITE
    
    def turn_on(self, color=Color.WHITE):
        self.is_on = True
        self.counter += 1
        self.color = color
        return f"ON ({color.name.title()})"
    
    def get_status(self):
        if self.is_on:
            if self.counter == 1:
                return f"Light turned ON ({self.color.name.title()})"
            else:
                return f"Light Already turned ON ({self.color.name.title()})"
        else:
            return "Light turned OFF"

    def turn_off(self):
        self.is_on = False
        self.counter = 0
        return "OFF"
    
    # def get_status(self):
    #     if self.is_on:
    #         if self.counter == 1:
    #             return f"{self.turn_on()} Light turned ON"
    #         else:
    #              return f"{self.turn_on()}Light Already turned ON"
    #     else:
    #         return "Light turned OFF"
   

# Smaet Lock implementation
class Lock(SmartDevice):
    def __init__(self):
        self.is_lock = False
        self.counter = 0

    def turn_on(self):
        self.is_lock = True
        self.counter += 1
        return "Lock"
    
    def turn_off(self):
        self.is_lock = False
        self.counter = 0
        return "Unlock"
    
    def get_status(self):
        if self.is_lock:
            if self.counter == 1:
                return "Door locked"            
            else:  
                return "Door Already Locked"    
        else:
            return "Door Unlocked"       


lock = Lock()
lock.turn_on()
# lock.turn_on()
# lock.turn_on()
# lock.turn_off()
print(lock.get_status())

light = Light()
light.turn_on()
print(light.get_status())
# print(light.color(1))
print(lock.get_firmware_version())
print(light.get_energy_usage())

# Usage
light.turn_on(Color.RED)  # Red light
print(light.get_status())  # "Light turned ON (Red)"
# light.turn_on()
# # print(light.get_status())
# light.turn_off()
# print(light.get_status())
# light.turn_off()
# print(light.get_status())
# light.turn_on()
# print(light.get_status())
