class a:
    def fun1(self):
        print("fun1")
class b:
    def fun2(self):
        print("fun2")
class c(a,b):
    def fun3(self):
        print("fun3")
q=c()
o=a()
p=b()
q.fun3()
q.fun2()
q.fun1()