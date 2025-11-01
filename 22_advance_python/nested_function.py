def full_info():
    def tell_name():
        print("jonh")
    
    def tell_age():
        print(45)

    def tell_country():
        print("USA")

    def tell_all():
        tell_name()
        tell_age()
        tell_country()

    return tell_all # returning a nested function

info = full_info()
info()

