# read the students.csv file and display the name and age of the student, the age is incremented by 1
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], int(row["age"]) + 1)
    
    