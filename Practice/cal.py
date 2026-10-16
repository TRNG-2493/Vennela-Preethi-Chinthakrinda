class Calculator:
    @staticmethod #this method can we used as utility method, 
    # we can call this method without creating an object of the class, we can call them with class name
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
#c1= Calculator()
#c1.add(10,20)
print(Calculator.add(10,20)) #we can call this method without creating an object of the class
print(Calculator.subtract(10,5)) #we can call this method without creating an object of the class