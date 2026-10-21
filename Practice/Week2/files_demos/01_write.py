try:
    file = open("output.txt","w")
    file.write("This is a test file.\n")
    file.write("It contains multiple lines of text.\n")
except Exception as error:
    print(error)
finally:
    if 'file' in locals() and not file.closed:
        file.close()