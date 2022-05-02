#You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

#Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

#For example, given the following board:

#[[f, f, f, f],[t, t, f, t],[f, f, f, f],[f, f, f, f]]
#and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else o
A=[["f", "f", "f", "f"],["t", "t", "f", "t"],["f", "f", "f", "f"],["f", "f", "f", "f"]]
visited=[[0 for i in range(len(A[0]))]for j in range(len(A))]
start=(3,0)
end=(0,0)
x=[1,-1,0,0]
y=[0,0,1,-1]
xi=[]
flag=0
c=0
xi.append(start)
visited[start[0]][start[1]]=1
if start==end:
    print(0)
else:
    def v(a,b,x,y):
        return  a>=0 and b>=0 and a<x and b<y
    while len(xi):
        k=len(xi)
        new=[]
        while k:
            s=xi.pop()
            for i in range(len(x)):
                if v(s[0]+x[i],s[1]+y[i],len(A[0]),len(A)) and visited[s[0]+x[i]][s[1]+y[i]]!=1 and A[s[0]+x[i]][s[1]+y[i]]!="t":
                    if s[0]+x[i]==end[0] and s[1]+y[i]==end[1]:
                        print(c+1)
                        flag=1
                        break
                    else:
                        new.append((s[0]+x[i],s[1]+y[i]))
                    visited[s[0] + x[i]][s[1] + y[i]]= 1
            if flag==1:
                break
            k-=1
        if flag==1:
            break
        c+=1
        xi=new
    if flag==0:
        print('null')



