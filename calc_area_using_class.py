#sending parameters to object using constructor
import math
class circle:
    def __init__ (self,r):
        self.r=r
    def printing(self):
        res=math.pi*r*r
        print("area of circle =",res)
class rectangle:
    def __init__ (self,l,b):
        self.l=l
        self.b=b
    def printing(self):
        print("area of rectangle=",l*b)
l=float(input())
b=float(input())
r=float(input())
o=circle(r)
o1=rectangle(l,b)
o.printing()
o1.printing()