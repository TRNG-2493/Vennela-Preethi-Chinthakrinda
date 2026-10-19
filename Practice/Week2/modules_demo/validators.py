MAX_USERNAME_LENGTH = 20

def is_valid_username(name):
    if not isinstance(name, str) or name == "":
        return False
    if len(name) > MAX_USERNAME_LENGTH:
        return False
    
    return name

if __name__ == "__main__": #this is not executed if we run main
    print(is_valid_username("Vennela"))

#now we have print in validators and if we run main, it executes main and validators, but we do not 
#to print the validators output right, so when we are creating a module
# we have a default dunder __main__