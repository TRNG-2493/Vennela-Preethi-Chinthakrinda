import csv

# reader function to read from csv file
try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row) # output is list
    
except FileNotFoundError as e:
    print(e)
    
# can also use DIctReader

"""reader = csv.DictReader(file)
for row in reader:
    print(row["name"], row["grade"])"""