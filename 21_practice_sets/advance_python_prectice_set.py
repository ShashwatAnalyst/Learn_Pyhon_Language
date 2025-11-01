# 1. Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".

def decorator(func):
    def wrapper():
        print("function is bieng called")
        func()
    return wrapper

def greet():
    print("hello!")

l = decorator(greet)
l()

# OR 

@decorator
def greet_with_decorator():
    print("hello!")

greet_with_decorator()

# 2. Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.

import time
def timer(func):
    def wrapper():
        start = time.time()
        print(func())
        end = time.time()
        time_taken = end - start
        print(time_taken)
    return wrapper

@timer
def sum():
    total = 0
    for i in range(1,1000001):
        total += i 
    return total

sum()

# 3. Create a class Employee with a private attribute _salary. Use @property to define a getter for salary. Use @salary.setter to prevent setting negative values (print a warning instead). Create an object and test by setting positive and negative salaries.


class Employee:
    def __init__(self , salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self , n):
        if n < 0 :
            print(f"Error! Salary can't be {n}")
        else:
            print(f"Salary has been changed to {n}")
            self.__salary = n
    
e = Employee(4000)
print(e.salary)
e.salary = 5000
print(e.salary)

# 4. Create a class MathUtils with:
# A @staticmethod called add(a, b) that returns a + b.
# A @classmethod called description(cls) that prints "This is a utility class for math operations."
# Call both methods without creating an object.

class MathUtils:
    def __init__(self):
        pass

    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")

m = MathUtils()
print(m.add(4,6))
m.description()

MathUtils.description()
print(MathUtils.add(4,8))

# 6. 

    # Create a class Book with attributes title and author.
    #     Implement __str__() so that printing the object displays "Title by Author".
    #     Implement __len__() so that len(book) returns the length of the title.

    # Create two Book objects and test these methods.

class Book:
    def __init__(self , title , author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"title of book is {self.title} and author of book is {self.author}"

    def __len__(self):
        return len(self.title)
    
b = Book("lemano travels" , "abarahm")
print(str(b))
print(len(b))


# 7. 
    # Use map() to convert [1, 2, 3, 4, 5] into their cubes.
    # Use filter() to get only even numbers from [10, 11, 12, 13, 14].
    # Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].

list1 = [1, 2, 3, 4, 5]

cube = list(map(lambda x:x*x*x,list1))


print(cube)


list2 = [10, 11, 12, 13, 14]

def even_only(x):
    if x %2 == 0:
        return True
    else:
        return False

from functools import reduce
even = list(filter(even_only,list2))

print(even)

list3 = [1, 2, 3, 4]

def prod_reduce(x,y):
    return x*y

prod = reduce(prod_reduce,list3)

print(prod)

# 9. 
    # Write a function sum_all(*args) that accepts any number of integers and returns their sum.
    # Write a function print_details(**kwargs) that prints key-value pairs passed as arguments



def num(*args):
    total = 0
    for i in args:
        total += i
    return total

print(num(2,21,23))

def user(**kwargs):
    for i,j in kwargs.items():
        print(f"{i}:{j}")


user(name="harry",id=21,sal=2000)









    



    