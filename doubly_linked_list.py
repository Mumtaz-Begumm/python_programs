class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll():
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def delatbeg(self):
        self.head=self.head.next
        self.head.prev=None
    def delatend(self):
        self.tail=self.tail.prev
        self.tail.next=None
    def printing(self):
        if self.head==None:
            return
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
l=[1,2,3,4,5]
l1=[2,4,6,8,10]
o=dll()
for i in l:
    o.insertatbeg(i)
    #o.insertatend(i)
o.printing()
o.delatbeg()
print("del at beg:")
o.printing()
print("del at end:")
o.delatend()
o.printing()
