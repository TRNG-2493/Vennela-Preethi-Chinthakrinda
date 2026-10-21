    #csv append 1 more row in this file
    
import csv

new_row=["Devi", 20, "A"]
with open("students_out.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)
    
# read the students.csv file and display the name and age of the student, the age is incremented by 1