class Employee:

    # here __init__ is dunder/magic method
    def __init__(self ,name, salary):
        self.name = name 
        self.salary = salary
    
    # here __str__ is dunder/magic method 
    def __str__(self):
        return f"the name is {self.name} , and salary is {self.salary}"
    
    # here __repr__ is dunder/magic method
    def __repr__(self):
        return f"name: {self.name} \nsalaary: {self.salary}"
    
    def __len__(self):
        return len(self.name)
    
    # and we have already seen __add__ dunder method in operator overloading in "17_oops\operator_overloading.py"


    
e = Employee("John cena" , 40000)
print(e.name)
print(e.salary)
print(str(e))
print(repr(e))
print(len(e))




