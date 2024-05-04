class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class cll:
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
        self.tail.next=self.head
        self.head.prev=self.tail
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
        self.tail.next=self.head
        self.head.prev=self.tail
    def printing(self):
        if self.head==None:
            return 
        else:
            i=self.head.next
            print(self.head.data)
            while i!=self.head:
                print(i.data)
                i=i.next
l=[1,2,3,4,5]
o=cll()
print("insert at beg:")
for i in l:
    o.insertatbeg(i)
o.printing()
print("insert at end:")
for i in l:
    o.insertatend(i)
o.printing()


        
