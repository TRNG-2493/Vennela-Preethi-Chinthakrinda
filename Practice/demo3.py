def my_decorator(func): #define once and use multiple times
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@my_decorator #decorator
def greet():
    print("Hello, welcome to the demo!")
    
@my_decorator 
def thankyou():
    print("Thank you for using the demo!")
       
greet()
thankyou()

# what is decorator
# a decorator is callable that takes a function as an argument - adds or changes the behaviour
# and returns a callable without changing the original functionality
# ex: @classmethod, @staticmethod

# can we create a decorator that works with function arguments - Yes.


