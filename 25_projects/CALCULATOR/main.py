
try:

    a = int(input("Enter first number: "))

    b = int(input("Enter Second number: "))

    print("what type of operation do you want to perform.\nPress + for Addition,\n - for Substraction,\n * for Multiplication,\n / for Division")

    o = input("Enter operator: ")

    if o == "+":
        print("The result is",a+b)
    elif o == "-":
        print("The result is",a-b)
    elif o == "*":
        print("The result is",a*b)
    elif o == "/":
        print("The result is",a/b)
    else:
        print("There was an Error")
   
except Exception as e:
    print("Enter a valid value of a and b")

