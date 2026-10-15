def greet():
    print("Hello, welcome to the function demo!")

def add(a,b):
    return a+b

def describe_person(name, age):
    print(f"{name} is {age} years old.")  
    
def sayhello(name,greeting ="Hello"):
    print(f"{greeting}, {name}!")
    
def add_all(*args):
    total=0
    for n in args:
        total+=n
    return total

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
def max_min(*numbers):
    return max(numbers), min(numbers) 

      
#call the function
greet() #default function call

result = add(5, 3)
print("The result is: ",result)

describe_person("Alice", 30) #postional parameters
describe_person(age=25, name="Bob") #keyword parameters
describe_person("Charlie", age=40) #mixing positional and keyword parameters

sayhello("Alice") #using default greeting
sayhello("Bob", greeting="Hi") #overriding default greeting
sayhello(name="Charlie", greeting="Hey") #using keyword arguments

print(add_all(1,2,3,4,5)) #arbitrary positional arguments (1 asterisk *)
print(add_all(1,2,3,4,5,6,7,8,9,10)) #arbitrary positional arguments

print_info(name="Alice", age=30, city="New York") #arbitrary keyword arguments (2 asterisks **)
print_info(name="Bob", occupation="Engineer") #arbitrary keyword arguments

print(max_min(1,2,3,4,5)) #result is a tuple

#lambda function demo
#lambda functions are anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression. The expression is evaluated and returned.
#syntax: lambda arguments: expression
lambda_add = lambda x, y: x + y
result = lambda_add(5, 3)
print("The result of lambda_add is: ", result)
print("The result of lambda_add is: ", (lambda x,y=10:x+y)(5))

#map(), filter(), reduce() demo
#map() applies a function to all items in an iterable (like a list) and returns
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers: ", squared)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers: ", even_numbers)
