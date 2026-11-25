# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        intuition: do bfs again, but this time take only the last element of the queue of that level.
        time : O(n), space: O(n), but instead of bfs where we pass through all nodes then encounter the one we want, we can instead do dfs and append the first node from the right, which is significantly faster for leaner trees and changes the space to O(h)
        '''
        ans=[]
        def dfs(x,depth):
            if not x:
                return 
            if len(ans)==depth:
                ans.append(x.val)
            dfs(x.right,depth+1)
            dfs(x.left,depth+1)

        dfs(root,0)
        return ans