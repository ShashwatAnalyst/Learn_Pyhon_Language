import os

a= os.listdir("dir")
print(a)

b = os.getcwd()
print(b)

c = os.path.exists("john")
print(c)

# os.remove("harry.txt")

os.rmdir("dir")