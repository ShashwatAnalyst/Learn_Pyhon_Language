a = int(input("enter a number: "))
b = int(input("enter second number: "))

if (b == 1 or a == 1):
    raise ValueError("i dont like 1")

print(a/b)