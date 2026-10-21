import csv
rows = [
    ["name", "age", "grade"],
    ["Alice", 20, "A"],
    ["Bob", 19, "B"],
    
]

with open("students_out.csv", "w",newline="") as file:
 #newline="" is to remove newline
    writer = csv.writer(file)
    writer.writerows(rows)
    #writerow - one rows
    
    
    #csv append 1 more row in this file