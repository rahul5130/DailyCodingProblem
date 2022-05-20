"""Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24."""
l=list(map(int,input().split()))
s=int(input())
l.sort()
m=[]
def com(l,s,n):
    if s<0:
        return
    if s==0:
        return n
    for i in range(len(l)):
        if s<l[i]:
            break

        k=com(l[1:],s-l[i],n+[l[i]])
        if k:
            return k
try:
    print(com(l,s,[])[::-1] )
except:
    print("Null")

#SPACECOMPLEXITY:O(2**N)
#TIMECOMPLEXITY:O(2**N)





