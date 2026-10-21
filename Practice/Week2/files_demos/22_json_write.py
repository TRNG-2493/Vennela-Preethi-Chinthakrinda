import json

student={
    "name" : "John Doe",
    "age" : 20,
    "major": "Computer Science",
    "courses": ["Python", "Data STructures"]

}

with open('studnet_out.json', 'w') as file:
    json.dump(student, file, indent=4)