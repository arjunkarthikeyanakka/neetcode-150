class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        n=r*c
        left,right=0,n-1
        while left<=right:
            m=left+(right-left)//2
            i,j=m//c,m-c*(m//c)
            val=matrix[i][j]
            # print(val,m,left,right)
            if val==target:
                return True
            elif val<target:
                left=m+1
            else:
                right=m-1
        return False