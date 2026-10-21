try:
    file = open("output.txt", "a")
    file.write("This is an appended line.\n")
except Exception as error:
    print(error)
    