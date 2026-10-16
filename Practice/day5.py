#class Student:
#    name = "Preethi"
#    age = 20
    
#s1=Student() #s1 is object of class Student, the members of class Student can be accessed using s1
# members are name and age, which are class variables
#print(s1.name)
#print(s1.age)

# why we need dunder method ?

class Student:
    school_name = "ABC School"
    def __init__(self,name,age,grade): #constructor #dunder method - takes the self parameter, the self parameter points to current object/instances of the class, self is a reference to the current object of the class
        self.name=name
        self.age=age
        self.grade=grade

    def __str__(self): #dunder method - returns the string representation of the object
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})" #returns the str value
    #when we use __str_ method, we can print the object and it will return the 
    # string representation of the object instead of memory location
    
    def __repr__(self): #dunder method - returns the string representation of the object 
        #this dunder method is used for debugging
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})" #returns the str value
    
    #def introduce(self):
     #   return f"My name is {self.name} and I am {self.age} years old and my grade is {self.grade}"
    
    @classmethod
    def change_school(cls, new_school_name): #class method, takes the class as parameter
        cls.school_name = new_school_name #changes the class variable
    
        
s1 = Student("Preethi", 20, "A")
s2 = Student("Ravi", 21, "B")
Student.change_school("XYZ School") #changes the class variable for all the objects of the class

#print(s1.name)
#print(s1.age)
#print(s1.grade)
print(s2.name, s2.age, s2.grade)
print(s1) #prints the memory location of the object
print(s2) #prints the memory location of the object
#print(repr(s1)) #prints the string representation of the object
print(s1.school_name)

#s1.introduce() #prints the introduction of the student 
# we call s1 on introduce method

# create a class name it as BankAccount, pascal cases
# initialize 2 variables, owner and balance, the class has 2 methods, deposit - which takes the parameter as amount
# and updates the balance adding the amount to balance
# 2nd method is showbalance whicg prints the owner name and curr balance.

class BankAccount:
    bank_name ="ABC bank" #class variable, this variable is shared by all the objects of the class
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def show_balance(self):
        print(f"Owner: {self.owner}, Current Balance: {self.balance}")
        
#s1=BankAccount("Preethi", 1000)
#s1.deposit(500)
#s1.show_balance()
#print(s1.bank_name) #prints the class variable, this variable is shared by all the objects of the class