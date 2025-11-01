class Point:

    def __init__(self , x, y):
        self.x = x
        self.y = y

    def sum(self, p): # Method overriding
        return Point((self.x + p.x),(self.y + p.y))
    
    def __add__(self,p): # Method overloading
        return Point((self.x + p.x),(self.y + p.y))
    
    def print_point(self):
        print(f"x is {self.x} y is {self.y}") 
    
p1 = Point(3,5)
p2 = Point(4,2)

p = p1.sum(p2) # this is working because of # Method overriding
p.print_point()

s = p1 + p2 # this is working because of # Method overloading
s.print_point()