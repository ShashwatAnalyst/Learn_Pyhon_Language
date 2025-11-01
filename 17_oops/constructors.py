class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond
        
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        return f"Employee Name : {self.salary}, Salary : {self.salary}, Bond : {self.bond}"

e1 = Employee(34000, "John Doe", 4)
print(e1.get_salary())
print(e1.get_info())