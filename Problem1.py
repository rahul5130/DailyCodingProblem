l=list(map(int,input().split()))
k=int(input())
d={}
for i in l:
    try:
        d[i]+=1
    except:
        d[i]=1
for i in d:
    d[i]-=1
    if k-i in d and d[i]>0:
        print("True")
        break
    d[i]+=1
else:
    print("False")
