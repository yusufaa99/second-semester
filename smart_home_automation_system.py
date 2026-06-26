from abc import ABC, abstractmethod
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

# Smart light
class Light(SmartDevice):
    def __init__(self):
        self.is_on = False
        self.counter = 0

    def turn_on(self):
        self.is_on = True
        self.counter += 1
        return "ON"
    
    def turn_off(self):
        self.is_on = False
        self.counter = 0
        return "OFF"
    
    def get_status(self):
        if self.is_on:
            if self.counter == 1:
                return "Light turned ON"
            else:
                 return "Light Already turned ON"
        else:
            return "Light turned OFF"

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
# light.turn_on()
# # print(light.get_status())
# light.turn_off()
# print(light.get_status())
# light.turn_off()
# print(light.get_status())
# light.turn_on()
# print(light.get_status())
