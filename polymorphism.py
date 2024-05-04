class a:
    def fun1(self):
        print("fun1")
class b:
    def fun2(self):
        print("fun2")
class c(a,b):
    def fun1(self):
        print("fun3")
q=c()
o=a()
p=b()
#q.fun3()  #functions have same name , so the last function gets executed
q.fun1()   #class gives importance to its own method
