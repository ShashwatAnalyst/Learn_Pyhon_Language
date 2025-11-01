# Map
a = [2,3,4,5,6,7,8]

b = list(map(lambda x : x *x,a)) # applying entire function to an iterable (list)

print(b)

# Filter
def greater_than_100(x):
    if x > 100:
        return True
    else:
        False

c = [80, 8498,477,486,79,43,3]

d = list(filter(greater_than_100,c))

print(d)

# Reduce

from functools import reduce
def add(a,b):
    return a +b

e = [44,43,22,221,45]

f = reduce(add,e)

print(f)



