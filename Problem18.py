"""Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them."""
from collections import deque
def printMax(arr, n, k):
    Qi = deque()
    for i in range(k):
        while Qi and arr[i]>arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(k,len(arr)):
        print(arr[Qi[0]],end=" ")
        while Qi and Qi[0]<=i-k:
            Qi.popleft()
        while Qi and arr[i]>arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    print(arr[Qi[0]])
arr = [4,2,1,3,2,1,9,4,3]
k = 3
printMax(arr, len(arr), k)

#TimeComplexity:o(n)
#SpaceComplexity:o(n)



