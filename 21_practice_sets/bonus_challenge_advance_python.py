# BONUS: 
    # Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.
    # Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.
    # Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing.


def decorator(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper
    

@decorator
def user(*args):
    total = 0
    for i in args:
        total += i
    return total

print(user(43,32,2))


class Vector:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,p):
        return Vector((self.x+p.x),(self.y+p.y))
    
a = Vector(2,3)
b = Vector(4,5)

s = a + b
print(f"({s.x},{s.y})")




while True:
    try:
        a = int(input("number 1: "))
        b = int(input("number 2: "))

        print(a/b)

    except Exception as e:
        print(e)




