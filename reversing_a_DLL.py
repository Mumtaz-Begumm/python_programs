class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
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
    def printing(self):
        if self.head==None:
            return
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
    def reversing(self):
        print("reversed ll is:")
        curr=self.head
        while curr:
            if curr.next==None:
                self.head=curr
            curr.next,curr.prev=curr.prev,curr.next
            curr=curr.prev
l=[1,2,3,4,5]
o=dll()
for i in l:
    o.insertatbeg(i)
o.printing()
o.reversing()
o.printing()
o.delatbeg()
o.delatend()

