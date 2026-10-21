# byte files, text files - 2 types of files
# byte files are binary - audio, video, pdf
# text - csv, py, java, txt files
# by default python writes in text file
# 1. opening a File
# 2. perform operations (purpose of opening - read, write, append (file modes))
# returns the file pointer
# 3. close the file handler

# a file is a resource, every resource opened shd be closed. 
# relative path - start from the root of project
# absolute path - complete path

try:
    file = open("notes1.txt", "r")
    
# r, w, a, r+
    #content = file.read()
    #print(content)
    #file.close()
    
    for line in file:
        print(line.strip()) # removes whitespaces
    
except FileNotFoundError as error:
    print(error)
finally:
    if 'file' in locals() and not file.closed:
        file.close()

# one challenge is memory intenser - for large files, so we read it line-by-line (print(line.strip()))