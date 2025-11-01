while True:
    try:
        a = int(input("enter a number: "))
        b = int(input("enter second number: "))


        print(a/b)
    
    except ValueError:
        print("very bad")

    except ZeroDivisionError:
        print("NOOO!")

    except Exception as e:
        print("something went wrong!", e)

