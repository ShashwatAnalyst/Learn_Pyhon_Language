def marks(**kwargs):
    for item in kwargs.keys():
        print(f"marks of {item} is {kwargs[item]}")

marks(harry=20,vishal=57,neha=46)