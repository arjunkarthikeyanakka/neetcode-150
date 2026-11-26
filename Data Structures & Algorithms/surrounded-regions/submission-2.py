class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        '''
        intuition: reverse the problem. Flood-fill from border 'O's to mark them safe ('I'),
        then flip remaining 'O' to 'X' and restore 'I' to 'O'.
        time: O(r*c), space: O(r*c) worst case (recursion stack)
        '''
        r,c=len(grid),len(grid[0])
        def out_of_bounds(x,y):
            return x>=r or y>=c or x<0 or y<0 or grid[x][y]!="O"
        def dfs(x,y):
            if out_of_bounds(x,y):
                return
            grid[x][y]='I'
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                dfs(nx,ny)
            
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="O" and (i==r-1 or j==c-1 or i==0 or j==0):
                    dfs(i,j)
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='O':
                    grid[i][j]='X'
                elif grid[i][j]=='I':
                    grid[i][j]='O'