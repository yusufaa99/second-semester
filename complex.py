class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def prints(self):
        print(f"{self.real}" + "+j" + f"{self.imaginary}")

    def add(self, c):
        self.real += c.real
        self.imaginary += c.imaginary

    def sub(self, c):
        self.real -= c.real
        self.imaginary -= c.imaginary
    
c1 = complex(20, 30)
c1.prints()
c2 = complex(15, 34)
c1.add(c2)
c1.prints()
c1.sub(c2)
c1.prints()
