#polymorphism - same method name diff functionality
class Animal:
    def sound(self):
        #print("Animal makes a sound.")
        pass
    
class Dog(Animal):
    def sound(self):
        print("Dog barks.")

class Cat(Animal):
    def sound(self):
        print("Cat meows.")
        
dog = Dog()
cat = Cat()
dog.sound()  # Output: Dog barks.
cat.sound()  # Output: Cat meows.
#calling same method on diff objects this is polymorphism - same method name diff functionality