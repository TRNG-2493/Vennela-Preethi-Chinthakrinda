with open("notes1.txt", "r") as file:
    content = file.read()
    print(content)

 # "with" is a context manager, we do not have to manually close it, it will taken care by compiler.
 