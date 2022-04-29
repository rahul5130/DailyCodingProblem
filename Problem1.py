#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?

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
