class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(9):
            c=0
            vis=set()
            for j in range(9):
                cell = board[i][j]
                if cell!='.':
                    c+=1
                    if cell in vis:
                        return False
                    vis.add(cell)
        # column check
        for i in range(9):
            c=0
            vis=set()
            for j in range(9):
                cell = board[j][i]
                if cell!='.':
                    c+=1
                    if cell in vis:
                        return False
                    vis.add(cell)
        # grid checks
        for i in range(0,9,3):
            for j in range(0,9,3):
                grid=[]
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l]!='.':
                            grid.append(board[k][l])
                s=set(grid)
                if len(s)!=len(grid):
                    return False
        return True