"""There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right."""

n=int(input())
m=int(input())
s=1
def f(s,i,j):
    if i==n-1 and j==m-1:
        return 1
    if i>=n or j>=n:
        return 0
    return f(s,i+1,j)+f(s,i,j+1)
print(f(s,0,0))

#SPACECOMPLEXITY:O(1)
#TIMECOMPLEXITY:O(2**N)





