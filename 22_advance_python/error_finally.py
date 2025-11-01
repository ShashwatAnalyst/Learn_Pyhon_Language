
def divide(a,b):
    try:
        print(a/b)
        return a/b
        
    
    except Exception as e:
        print(e)
        return None
        

    finally:
        print("function completed!")

a = int(input("enter a number: "))
b = int(input("enter second number: "))

divide(a,b)