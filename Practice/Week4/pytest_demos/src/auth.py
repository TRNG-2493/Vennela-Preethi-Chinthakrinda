USERS ={"admin":"admin123",
        "guest":"guest123"}

def login(username,password):
    return USERS.get(username) == password