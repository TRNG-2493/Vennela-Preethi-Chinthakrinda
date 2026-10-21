try:
    with open("notes.txt", "w") as file:
        file.write("This is a new line.\n")
        print("Line appended successfully")
except Exception as error:
    print(f"An error occured: {error}")