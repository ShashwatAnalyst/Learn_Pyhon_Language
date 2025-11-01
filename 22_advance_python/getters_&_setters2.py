class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    
    @property # we have created this method as a getter property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @first_name.setter #name of function should be same for setter and getter property decorator
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e = Employee("john wick" , 500000)
e.kills = 1000

print(e.name,e.salary,e.kills)
print(e.first_name)
e.first_name = "jack"
print(e.name)
