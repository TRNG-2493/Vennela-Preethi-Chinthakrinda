class Animal:
    def eat(self):
        print("Animal is eating.")
    
class Dog(Animal): #child class, inherits from Animal class
    def bark(self):
        print("Dog is barking.")
        
dog = Dog()
dog.eat()  # Inherited method from Animal class
dog.bark()  # Method from Dog class