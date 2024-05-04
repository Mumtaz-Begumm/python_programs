class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            i=self.head
            while i:
                i=i.next
            i.next=new
    def delatbeg(self):
        i=self.head
        self.head=self.head.next
        i.next=None
    def delatend(self):
        i=self.head
        while i.next.next:
            i=i.next
        i.next=None
    def printing(self):
        if self.head==None:
            return 
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next


l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()
print("del at beg:")
o.delatbeg()
o.printing()
print("del at end")
o.delatend()
o.printing()
