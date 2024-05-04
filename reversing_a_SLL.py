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
    def reversing(self):
        print("reverse of sll is:")
        prev=None
        curr=self.head
        nxt=self.head.next
        while curr:
            curr.next=prev
            prev=curr
            curr=nxt
            if nxt:
                nxt=nxt.next
        self.head=prev
    def printing(self,data):
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
    #o.insertatend(i)
o.printing(i)
o.reversing()
o.printing(i)
