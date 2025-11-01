def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(5)
def say_hello(name):
    print(f"hello {name}!")

say_hello("harry")