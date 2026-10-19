try:
    a=10
    #b=0
    b = int(input("Enter a number to divide by: "))

    result = a/b
    print(result)
    
#except ZeroDivisionError:
#    print("You cannot divide by zero")
  
except ZeroDivisionError as error:
    print("You cannot divide by zero")
    # used for debugging, more detailed output of error
    #print(error)
    #print(type(error).__name__)
    #print(error.args)
    
except ValueError as error:
    print("You must enter a number")
    
#we can have multiple except block

else: # only executed if no exception is raised
    print("Division successful")
    print("Result is: ", result)
    
finally: #always executed
    print("This is the end of the program")