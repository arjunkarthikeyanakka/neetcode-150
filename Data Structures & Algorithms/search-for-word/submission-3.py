class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        intuition: try every cell as a start. From a cell that matches word[idx], DFS into
        its 4 neighbors for word[idx+1]. Mark the cell as visited so a path can't reuse it,
        and un-mark after exploring (backtrack) so other paths can use it. Success when idx == n.
        time: O(r*c*3^n)  (4 choices at the first step, then 3 since the previous cell is visited)
        space: O(n) recursion depth + visited set
        This is NP-hard, so we cant solve this better than this...
        '''
        r,c=len(board),len(board[0])
        n=len(word)
        vis=set()
        def dfs(x,y,idx=0):
            if idx==n:
                return True
            if x<0 or y<0 or x>=r or y>=c or (x,y) in vis or word[idx]!=board[x][y]:
                return False
            vis.add((x,y))
            found= dfs(x+1,y,idx+1) or dfs(x-1,y,idx+1) or dfs(x,y+1,idx+1) or dfs(x,y-1,idx+1)
            vis.remove((x,y))
            return found
        for i in range(r):
            for j in range(c):
                if dfs(i,j):
                    return True
        return False