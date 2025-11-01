try:
    a = int(input("enter a number: "))
    b = int(input("enter second number: "))

    print(a/b)

except Exception as e:
    print("something went wrong!", e)



else:
    print("👍")
