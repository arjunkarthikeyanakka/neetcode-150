from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def ps():
            for i in range(r):
                print(grid[i][:])
        r,c=len(grid),len(grid[0])
        vis=set()
        dq=deque()
        def out_of_bounds(x,y):
            return (x,y) in vis or x>=r or y>=c or x<0 or y<0 or grid[x][y]&1==0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    vis.add((i,j))
                    dq.append((i,j))
        sec=-1
        while dq:
            l=len(dq)
            for _ in range(l):
                x,y=dq.popleft()
                grid[x][y]=2
                if not out_of_bounds(x+1,y):
                    vis.add((x+1,y))
                    dq.append((x+1,y))
                if not out_of_bounds(x-1,y):
                    vis.add((x-1,y))
                    dq.append((x-1,y))
                if not out_of_bounds(x,y+1):
                    vis.add((x,y+1))
                    dq.append((x,y+1))
                if not out_of_bounds(x,y-1):
                    vis.add((x,y-1))
                    dq.append((x,y-1))
            # ps()
            # print('...')
            sec+=1
        fresh=False
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return -1
        return max(0,sec)