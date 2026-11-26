from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        intuition: multi-source BFS from all rotten oranges; each level is one minute.
        Mark cells rotten on push so none is queued twice. If fresh oranges remain, -1.
        time: O(r*c), space: O(r*c) worst case (queue)
        '''
        r,c=len(grid),len(grid[0])
        dq=deque()
        def out_of_bounds(x,y):
            return x>=r or y>=c or x<0 or y<0 or grid[x][y]!=1
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    dq.append((i,j))
        sec=0
        while dq:
            l=len(dq)
            for _ in range(l):
                x,y=dq.popleft()
                if not out_of_bounds(x+1,y):
                    grid[x+1][y]=2
                    dq.append((x+1,y))
                if not out_of_bounds(x-1,y):
                    grid[x-1][y]=2
                    dq.append((x-1,y))
                if not out_of_bounds(x,y+1):
                    grid[x][y+1]=2
                    dq.append((x,y+1))
                if not out_of_bounds(x,y-1):
                    grid[x][y-1]=2
                    dq.append((x,y-1))
            sec+=1 if dq else 0 # counting only when something is infected.
        fresh=False
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return -1
        return max(0,sec)