class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, age):
        # Call the constructor of the parent class
        super().__init__(name)
        self.age = age
        
student = Student("Alice", 20)
print(student.name)  # Output: Alice
print(student.age)   # Output: 20