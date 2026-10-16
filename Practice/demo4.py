def another_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("AFter the function call")
    #return wrapper   
        
@another_decorator
def add(a,b):
    return a+b

result = add(5,3)
print(f"result of addition: {result}")