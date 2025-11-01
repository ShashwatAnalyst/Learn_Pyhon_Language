def sum(*args):
    total = 0
    for i in args:
        total += i 
    return total 

print(sum(28,21,12,3))