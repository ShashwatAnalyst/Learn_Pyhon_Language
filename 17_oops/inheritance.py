class Animal:
    location = "USA"
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Generic animal sound")

# a = Animal("Dog")
# a.speak()

class Dog(Animal):
    def speak(self):
        super().speak() # we are using the speak method from parent class
        print("Woof!")

d = Dog("Tom")
d.speak()
print(d.location)