#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

#For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

k=input()
l=int(input())
s={}
x=set()
st=0
e=0
high,low=0,0
for i in range(len(k)):
    x.add(k[i])
    try:
        s[k[i]]+=1
    except:
        s[k[i]]=1
    while len(x)>l:
        s[k[low]]-=1
        if s[k[low]]==0:
            x.remove(k[low])
        low+=1
    high+=1
    if e-st<high-low:
        e=high
        st=low
print(e-st)

