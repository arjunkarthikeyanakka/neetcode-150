# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        intuition: just maintain a passing variable that has the max value of nodes in the current path and if you notice it less than or equal to the current node, you count it as a good node. time : O(n) - you'll visit each node once, space : O(h).
        '''
        ans=0
        def dfs(x,curr):
            nonlocal ans
            if not x:
                return
            dfs(x.left,max(curr,x.val))
            dfs(x.right,max(curr,x.val))
            if curr<=x.val:
                ans+=1
        dfs(root,-1e9)
        return ans