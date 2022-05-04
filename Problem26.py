#Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

#The list is very long, so making more than one pass is prohibitively expensive.

#Do this in constant space and in one pass.

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
        self.temp=None
    def add(self,num):
        if self.head==None:
            self.head=node(num)
            self.temp=self.head
        else:
            self.temp.next=node(num)
            self.temp=self.temp.next
    def printl(self):
        k=self.head
        while k:
            print(k.data)
            k=k.next
s=ll()
s.add(1)
s.add(2)
s.add(11)
s.add(211)
s.add(21)
s.add(31)
s.add(92)
s.add(22)
k=int(input())
temp=s.head
while k>0:
    temp=temp.next
    k-=1
temp2=s.head
while temp.next:
    temp=temp.next
    temp2=temp2.next
temp2.next=temp2.next.next
s.printl()

#TimeComplexity:o(n)
#SpaceComplexity:o(1)


