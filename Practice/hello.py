print("Hello! This is testing")

#list
student = ["Alice", "Preethi", "Bob", "Dannie"]
student[1] = "Vennela Preethi"
student.append("Charlie")
print(student)
print(student[0])
print(student[-1])
print(student[1:3])
print(student[::-1])

#tuple
point = (1,2)
x,y = point
print(x)
print(y)

#set
setA={1,2,3,4,5}
setB={4,5,6,7,8}
print(setA)
print(setB)
setA.add(9)
print(setA)
setA.remove(2)
print(setA)

#dictionary - key value pairs
person = {"name":"Alice", "age":30, "city":"New York"}
print(person)
print(person["name"])
print(person["age"])
print(person["city"])

person["city"] = "Toronto"
print(person)
print(person.items())

for key in person:
    print(key)

for value in person.values():
    print(value)
    
for key, value in person.items():
    print(key, value)
    
    
#list comprehension
squared_numbers=[x**2 for x in range(10) if x%2==0]
print(squared_numbers)