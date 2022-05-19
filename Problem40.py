"""Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space."""

s=list(map(int,input().split()))
r=0
for i in range(32):
    k=(1<<i)
    m=0
    for j in range(len(s)):
        if k&s[j]:
            m+=1
    if m%3!=0:
        r+=k
print(r)
#TIMECOMPLEXITY:O(N)
#SPACECOMPLEXITY:O(1)
