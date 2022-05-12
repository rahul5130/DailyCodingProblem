"""The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them."""

def f(a,b,c,d,m):
    if c>=len(a):
        return len(b)-d
    if d>=len(b):
        return len(a)-d
    if m[c][d]!=-1:
        return m[c][d]
    if a[c]==b[d]:
        m[c][d]=f(a,b,c+1,d+1,m)
        return m[c][d]
    if a[c]!=b[d]:
        m[c][d]=1+min(f(a,b,c+1,d+1,m),f(a,b,c+1,d,m),f(a,b,c,d+1,m))
        return m[c][d]
a="kitten"
b="sitting"
m=[[-1 for i in range(len(b))]for j in range(len(a))]
#m is used for memoization

print(f(a,b,0,0,m))


#Timecomplexity:o(m*n)
#spacecomplexity:o(m*n)
