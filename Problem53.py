"""Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it."""

def enqueue(i,m,l):
    l.append(i)

    return  m,l

def dequeue(m,l):
    if len(m)==0:
        m=l[::-1]
        l=[]

    t=m.pop()
    return t,m,l
m=[]
l=[]
m,l=enqueue(1,m,l)
m,l=enqueue(3,m,l)
t,m,l=dequeue(m,l)
print(t)
m,l=enqueue(8,m,l)
t,m,l=dequeue(m,l)
print(t)
t,m,l=dequeue(m,l)
print(t)



#SPACECOMPLEXITY:O(N)
#TIMECOMPLEXITY : O(N)








