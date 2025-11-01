
def tell_name():
    print("john")

def tell_age():
    print(45)

def tell_country():
    print("USA")

def tell_info(func1,func2,func3):
    func1()
    func2()
    func3()

def full_info(func1,func2,func3,func4):
    func4(func1,func2,func3)

full_info(tell_name,tell_age,tell_country,tell_info)