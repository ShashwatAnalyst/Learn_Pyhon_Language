# 5.# Write a program that asks the user to enter a number and handles:
    #     ValueError if the input is not a number
    #     ZeroDivisionError if you try to divide by zero

    # Create a custom exception NegativeNumberError and raise it when the user enters a negative number.

class NegativeNumberError(Exception):
    pass

while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a/b)

    except ValueError:
        print("not good")

    except ZeroDivisionError:
        print("do not do this")

    if a<0 or b<0:
        raise NegativeNumberError("i dont want negative number")