def Decorators(func):
    def wrapper():
        print("going to execute function ...")
        func()
        print("function executed!")
    return wrapper


def say_hello():
    print("Hello!")
f = Decorators(say_hello)
f()
# OR
@Decorators
def hello():
    print("Hello!")

hello()
