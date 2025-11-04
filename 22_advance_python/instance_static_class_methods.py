class Employee:
    company = "HP"
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    
    # Instence Method (default)
    def print_info(self):
        print(f"the name is {self.name} and salary is {self.salary}")

    def sum(self,a,b):
        return a+b
    # OR
    # Static Method (works like a regular function)
    @staticmethod 
    def sum2(a,b):
        return a+b
    
    # Class Method
    @classmethod
    def print_company(self):
        print(self.company)

    @classmethod
    def change_company(self , new_company):
        self.company = new_company
        

e1 = Employee("harry" , 20000)
e2 = Employee("john" , 60000)

# e1.print_info()
# e2.print_info()
# print(e1.sum(12,23))
# print(e2.sum2(3,6))
e1.print_company()
e1.change_company("asus")
e1.print_company()
