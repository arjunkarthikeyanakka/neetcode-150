from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=(1<<31)-1
        r,c=len(grid),len(grid[0])
        def out_of_bounds(x,y):
            return (x,y) in vis or x>=r or y>=c or x<0 or y<0 or grid[x][y]<=0

        def bfs():
            while dq:
                l=len(dq)
                for _ in range(l):
                    cell=dq.popleft()
                    x,y=cell[0],cell[1]
                    grid[x][y]=min(cell[2],grid[x][y])
                    if not out_of_bounds(x+1,y):
                        vis.add((x+1,y))
                        dq.append((x+1,y,cell[2]+1))
                    if not out_of_bounds(x-1,y):
                        vis.add((x-1,y))
                        dq.append((x-1,y,cell[2]+1))
                    if not out_of_bounds(x,y+1):
                        vis.add((x,y+1))
                        dq.append((x,y+1,cell[2]+1))
                    if not out_of_bounds(x,y-1):
                        vis.add((x,y-1))
                        dq.append((x,y-1,cell[2]+1))
        dq=deque()
        vis=set()
        for x in range(r):
            for y in range(c):
                if grid[x][y]==0:
                    vis.add((x,y))
                    dq.append((x,y,0))
        bfs()