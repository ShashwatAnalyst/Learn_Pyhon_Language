# 1. write a greet function to print "hello python learners!" when its called
def greet():
    print("hello python learners!")

greet()

# 2. write a function which takes two args (first,last) and returns a string in the format "first last"

def full_name(first,last):
    return f"{first} {last}"

print(full_name("shashwat","singh"))

# 3. write a function which takes values of length and returns area the area of rectangle with default width = 10

def area(l , w = 10):
    a = l * w
    return f"{a} m.sq"

print(area(3))

# 4. write a lambda function that adds two numbers and test it 

sum = lambda a,b: a + b 

print(sum(3,5))

# 5. write a lambda function to return the list of square of list [1,2,3,4,5] using map function 

l = [1,2,3,4,5]

print(list(map(lambda x:x**2,l)))

# 6. write a recursive function to calculate factorial of n 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1)*n

print(factorial(6))

# 7. write a recursive function sum_of_digits(n) which returns sum of digits of a number 

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)

print (sum_of_digits(456))

# 8. calculate the square root of 144 and value of sin(90) using math module

import math

sqrt = math.sqrt(144)

print(sqrt)

sin90 = math.sin(math.radians(90))

print(sin90)

# 9. use requests module to fetch data from https://api.github.com

import requests 
a = requests.get("https://api.github.com/")
print(a.json())

# 10. write a recursive function fabonacci(n) that returns n's fabonacci number

"""
def fabonnaci(n):
    if (n == 0 or n == 1):
        return n
    return fabonnaci(n-2)+ fabonnaci(n-1)

print(fabonnaci(5))
"""

# 11. write a recursive function fabonacci(n) that print first n fabonacci numbers

def fabonnaci(n):
    def fab(k):
        if (k == 0 or k == 1):
            return k
        return fab(k-2)+ fab(k-1)
    for i in range(n):
        print(fab(i + 1))

fabonnaci(6)

# 12. write a function safe_divide(a,b) that divides a/b but if b = 0 it returns cannot divide my 0

def safe_divide(a,b):
    if b == 0:
        return "cannot divide my 0"
    return a/b

print(safe_divide(6,3))

# 13. create a my_utils.py module to create an is_even(n) function
import my_utils

print(my_utils.is_even(3))