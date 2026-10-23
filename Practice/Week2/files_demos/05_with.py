try:
    with open("notes.txt", "w") as file:
        file.write("This is a new line.\n")
        print("Line appended successfully")
except Exception as error:
    print(f"An error occured: {error}")
    
# when we open an existing file in w mode, it will override the existing content

# write a program that takes a message as input from the user writes it to a file and displays the same the message