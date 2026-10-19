#print("Hello") #stntax error happens at compile time

#number=int("abc")
#print(number) # this is runtime error
# exception is an abnormall condi that disturbs the normal flow of execution and program terminates
# python runtime creates an exception object, if there is no handler to encounter that exception it tracebacks to the function call, in order to work with exceptions we use handlers, it is about excepi=tion hnadling the comdition so that the program is not disturbed and ternminate gracefully, 
# if no exception handing the program will end arubptly

# try except block in python

def parse_price(text):
    return float(text)

def total(prices):
    result =0
    for p in prices:
        result += parse_price(p)
    return result    

print(total(['1.2', '2.3', '3.4',"hello"]))