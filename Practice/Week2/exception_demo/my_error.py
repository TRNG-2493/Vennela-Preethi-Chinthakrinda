class InvalidAgeError(Exception):
    def __init__(self,age):
        self.age=age
        self.message= f"Invalid age: {age}. Age must be greater than or equal to 18"
        super().__init__(self.message)
        
        
