# Class: Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name etc.

# Object: Specific instance create from the template (class) Eg. form that contains the data for John Doe

class Employee:
    company = "HP"
    
    def salary(self):
        return 34000
    
e1 = Employee()
print(e1.company)
print(e1.salary())

e2 = Employee()
print(e2.company)
print(e2.salary())


