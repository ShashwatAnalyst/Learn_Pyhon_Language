class Employee:
    company = "BMW" # class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary # instance attribute
        self.name = name # instance attribute
        self.bond = bond # instance attribute
        self.company = company # instance attribute
        
e1 = Employee(34000, "John Doe", 4, "Tesla")
print(e1.company) # prints instance attribute
print(Employee.company) # prints class attribute

# to get all methords used in the object
print(dir(e1))