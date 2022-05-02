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

    if n==0:
        return 1
    if n<0:
        return 0
    return count(n-1)+count(n-2)
print(count(n))

