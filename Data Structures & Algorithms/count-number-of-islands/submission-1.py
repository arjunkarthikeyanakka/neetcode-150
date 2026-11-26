class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        intuition: scan every cell; each unvisited '1' starts a new island. DFS floods
        the whole island so it is counted once.
        time: O(r*c), space: O(r*c) worst case (recursion stack)
        '''
        r,c=len(grid),len(grid[0])
        islands=0
        def out_of_bounds(x,y):
            return x>=r or y>=c or x<0 or y<0
        def dfs(x,y):
            if out_of_bounds(x,y) or grid[x][y]=="0":
                return
            if grid[x][y]=="1":
                grid[x][y]="0"
                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y-1)
                dfs(x,y+1)

        for x in range(r):
            for y in range(c):
                if grid[x][y]=='1':
                    dfs(x,y)
                    islands+=1

        return islands