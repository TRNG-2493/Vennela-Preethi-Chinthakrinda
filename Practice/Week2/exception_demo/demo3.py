from my_error import InvalidAgeError
try:
    age = int(input("Enter your Age: "))
    # custom exception
    if age < 18:
        raise InvalidAgeError.InvalidAgeError(age=age)
    
    # raising an exception - based on some condition we can creating a exc object and hadning it to runtime
    
    print("Your Age is: ", age)
    
#except ValueError as error:
#    print("You must enter a number")
    
except InvalidAgeError as error:
    print("You must be 18 or older to proceed")    
    print(error)
# custom exception are created by dev to handle business exceptions

