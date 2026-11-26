class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        each land cell you return 1+its neighbouring dfs cells and maximize this.
        time : O(r*c)
        space : O(r*c)
        '''
        r,c=len(grid),len(grid[0])
        mx=0
        def out_of_bounds(x,y):
            return x>=r or y>=c or x<0 or y<0
        def dfs(x,y):
            if out_of_bounds(x,y) or not grid[x][y]:
                return 0
            if grid[x][y]:
                grid[x][y]=0
                return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y-1) + dfs(x,y+1) 
        for x in range(r):
            for y in range(c):
                if grid[x][y]:
                    curr=dfs(x,y)
                    mx=max(mx,curr)
        return mx