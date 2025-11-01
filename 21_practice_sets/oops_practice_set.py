# 1. create a class car with a method drive() that prints "car is moving" , create an oject of car and call drive()

class Car:

    def drive(self):
        print("car is moving")

c = Car()
c.drive()

# 2. Create a class Person with a constructor ( __init__ ) that accepts name and age as arguments and stores them as instance attributes. Create an object and print the person’s name and age.

class Person:

    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def print_person(self):
        print(f"person's name is {self.name} and age is {self.age}")

p = Person("harry",40)
print(f"person's name is {p.name} and age is {p.age}")
# OR
p.print_person()

# 3.Create a base class Animal with a method sound() that prints "Some sound" . Create a derived class Dog that overrides sound() to print "Bark!" . Create an object of Dog and call sound() .

class Animal:
    def sound(self):
        print("some sound")

class Dog:
    def sound(self):
        print("bark!")

a = Animal()
a.sound()

d = Dog()
d.sound()