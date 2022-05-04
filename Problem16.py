#You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
#record(order_id): adds the order_id to the log
#get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
#You should be as efficient with time and space as possible.
class ecommerce:
    def __init__(self,n):
        self.l=[0 for i in range(n)]
        self.n=n
        self.i=0
    def record(self,order_id):
        if self.i<self.n:
            self.l[self.i]=order_id
        else:
            self.i%=self.n
            self.l[self.i] = order_id
        self.i+=1
    def get_last(self,n):
        return self.l[self.i-n]
s=ecommerce(3)
s.record(2)
s.record(3)
s.record(4)
s.record(1)
print(s.get_last(1))
#gives output as 1

#for both record and get_last function complexities are same i.e
#TimeComplexity:o(1)
#SpaceComplexity:o(1)


