# Walrus operator

def a_fucking_function():
    print("i am a funcking function's print statement")
    print("i am a funcking function's print statement")
    print("i am a funcking function's print statement")
    return 70

# if (a_fucking_function() > 10):
#     print(a_fucking_function())

# else:
#     print("i am not good enough")

# instead write 

# a = a_fucking_function()
# if (a > 10):
#     print(a)

# else:
#     print("i am not good enough")

# OR Using Walrus operator ":="

if (a:= a_fucking_function() > 10):
    print(a)

else:
    print("i am not good enough")

