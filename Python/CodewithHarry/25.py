class Calculator:
    def __init__(self, num):
        self.num = num
    def sq(self):
        print(f"The square of {self.num} is {self.num * self.num}")
    def cube(self):
        print(f"The cube of {self.num} is {self.num * self.num * self.num}")
    def sqrt(self):
        print(f"The sqrt of {self.num} is {(self.num)**1/2}")
    
    @staticmethod
    def greet():
        print(f"Hello there")
number = Calculator(4)
number.greet()
number.sq()
number.cube()
number.sqrt()