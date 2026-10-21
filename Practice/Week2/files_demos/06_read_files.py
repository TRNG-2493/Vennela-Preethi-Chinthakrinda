try:
    with open("notes.txt", "r", encoding="utf-8") as file:
        print(file.tell()) # current position in the file
        file.readline() # read the first line
        print(file.tell()) # current position after reading a line
        file.readline() # read the second line
        print(file.tell())
        file.seek(0) # move back the pointer to the beginning of the file
        #file.seek(10)
except FileNotFoundError as error:
    print(error)