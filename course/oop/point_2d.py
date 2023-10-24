import math

class Point2D:
    
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance_to_other(self, other:'Point2D'):
        
        a = other.x
        b = other.b
        x = self.x
        y = self.y
        ax = a * x
        bx = b * x
        ay = a * y
        by = b * y
        
        return math.sqrt((ax - bx)**2 + (ay - by)**2)
    
point_a = Point2D(3, 5)
print(type(point_a))

