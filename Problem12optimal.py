

#There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

#For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
n=int(input())
l=[1,2]
def count(n):
    if n==0 or n==1 :
        return n
    a,b=1,1
    for i in range(2,n+1):
        a,b=b,a+b
    return b
print(count(n))

#TimeComplexity:o(n)
#SpaceComplexity:o(1)


