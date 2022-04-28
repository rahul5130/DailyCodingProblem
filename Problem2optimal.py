l=list(map(int,input().split()))
s=[1]*len(l)
p=1
for i in range(1,len(l)):
        s[i]*=(p*l[i-1])
        p*=l[i-1]
p=1
for i in range(len(l)-2,-1,-1):
        s[i]=s[i]*p*l[i+1]
        p*=l[i+1]
print(s)



