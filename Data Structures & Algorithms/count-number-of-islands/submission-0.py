class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c=len(grid),len(grid[0])
        vis=set()
        islands=0
        def out_of_bounds(x,y):
            return x>=r or y>=c or x<0 or y<0
        def dfs(x,y):
            if out_of_bounds(x,y) or grid[x][y]=="0" or (x,y) in vis:
                return
            vis.add((x,y))
            if grid[x][y]=="1":
                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y-1)
                dfs(x,y+1)

        for x in range(r):
            for y in range(c):
                if grid[x][y]=='1' and (x,y) not in vis:
                    dfs(x,y)
                    islands+=1

        return islands