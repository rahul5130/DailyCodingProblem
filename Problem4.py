#Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#You can modify the input array in-place.
l=list(map(int,input().split()))
for i in range(1,len(l)):
    while l[i]<len(l)-1 and l[i]>0 and l[i]!=l[l[i]-1]:

        temp=l[i]
        l[i]=l[l[i]-1]
        l[temp-1]=temp
for i in range(len(l)):
    if i!=l[i]-1:
        print(i+1)
        break
else:
    print(len(l)+1)


