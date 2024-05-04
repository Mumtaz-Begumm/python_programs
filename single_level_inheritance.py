class a:
    def fun1(self):
        print("fun1")
class b(a):
    def fun2(self):
        print("fun2")
o=a()
p=b()
p.fun2()
p.fun1()  