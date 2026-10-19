MAX_USERNAME_LENGTH = 20

def is_valid_username_1(name):
    if not isinstance(name, str) or name == "":
        return False
    if len(name) > MAX_USERNAME_LENGTH:
        return False
    
    return name