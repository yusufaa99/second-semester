import math
class Exception_handling:
    def __init__(self):
        pass
    
    def div(self, dividend, divisor):
        # self.dividend = dividend
        # self.divisor = divisor

        try:
            self.dividend = int(dividend)
            self.divisor = int(divisor)
            result = self.dividend / self.divisor
            exp = math.exp(1000000)
            print(exp)
        except OverflowError as e:
            print(e)
        except ZeroDivisionError as e1:
            print(F"{self.dividend} cannot be divided by {self.divisor}", e1)
        except ValueError as e2:
            print("invalid input", e2)
        else:
            print(result)
        finally:
            print("Complete Execution")
    

exe = Exception_handling()

exe.div(10,"5")