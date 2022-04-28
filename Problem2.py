l=list(map(int,input().split()))
s=[1]*len(l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        s[i]*=l[j]
for i in range(len(l)):
    for j in range(i-1,-1,-1):
        s[i]*=l[j]
print(s)



