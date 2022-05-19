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
