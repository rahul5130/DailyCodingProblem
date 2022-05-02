#Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

#For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

#In this example, assume nodes with the same value are the exact same node objects.

#Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

# ASSUMING H1 AND H2 AS HEADS OF TWO LLS.
# NEXT INDICATES NEXT LOCATION AND DATA GIVES VALUE AT THAT LOCATION.
temp1=H1
temp2=H2
c1,c2=0,0
while temp1:
    c1+=1
    temp1=temp1.next
while temp2:
    c2+=1
    temp2=temp2.next
if c1>c2:
    k=c1-c2
    while k>0:
        H1=H1.next
        k-=1
else:
    k=c2-c1
    while k>0:
        H2=H2.next
        k-=1
while H1:
    if H1==H2:
        print(H1.data)
        break
    else:
        H1=H1.next
        H2=H2.next


