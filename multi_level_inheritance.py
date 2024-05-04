class a:
    def fun1(self):
        print("fun1")
class b(a):
    def fun2(self):
        print("fun2")
class c(b):
    def fun3(self):
        print("fun3")
q=c()
o=a()
p=b()
q.fun3()
q.fun2()
q.fun1()