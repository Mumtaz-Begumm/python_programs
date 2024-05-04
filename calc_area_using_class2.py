#sending parameters to function
class circle:
    def printing(self,r):
        res=3.142*r*r
        print("area of circle =",res)
class rectangle:
    def printing(self,l,b):
        print("area of rectangle=",l*b)
l=float(input())
b=float(input())
r=float(input())
o=circle()
o1=rectangle()
o.printing(r)
o1.printing(l,b)