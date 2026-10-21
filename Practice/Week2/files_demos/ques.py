# write a program that takes a message as input from the user writes it to a file and displays the same the message

message = input("Enter your message: ")
try:
    file = open("msg.txt","w")
    file.write(message)
except Exception as error:
    print(error)
finally:
    if 'file' in locals() and not file.closed:
        file.close()

file = open("msg.txt", "r")
content = file.read()
print(content)
file.close()

# ways to read files - IMP
# content = file.read()
# first_line = file.readline()
# lines - file.readlines()
