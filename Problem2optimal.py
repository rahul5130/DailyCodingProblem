#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?


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



