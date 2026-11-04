def get_user():
    return "John"

# welcome func taj=kes argument of above func
def welcome(user_getter=get_user):
    return "Hello " + user_getter()
    
    