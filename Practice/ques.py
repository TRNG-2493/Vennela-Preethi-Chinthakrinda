#create a class employee which is inherited in 2 classes, fulltime employee and parttime employee
# a fulltime receives fixed monthly sal and benefits, a parttime emp earns based on hourly rate
# and no of hours, polymor - calculate sal

class Employee:
    def __init__(self,name):
        self.name = name
    def calculate_salary(self):
        pass
    
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary, benefits):
        super().__init__("Full Time Employee")
        self.monthly_salary = monthly_salary
        self.benefits = benefits
        
    def calculate_salary(self):
        return self.monthly_salary + self.benefits

class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        super().__init__("Part Time Employee")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
print(FullTimeEmployee.__name__)
ft=FullTimeEmployee(4000, 100)
print("Full time Salary: ",ft.calculate_salary())
print(PartTimeEmployee.__name__)
pt=PartTimeEmployee(20, 100)
print("Part time Salary: ",pt.calculate_salary())