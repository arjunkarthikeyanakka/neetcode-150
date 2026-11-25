# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        intuition : use a NL var that will calc the sum of left and right heights of each node. Time : O(n), space : O(h)
        '''
        ans=0
        def h(x):
            nonlocal ans
            if not x:
                return 0
            l,r=h(x.left),h(x.right)
            ans=max(ans,l+r)
            return 1+max(l,r)
        h(root)
        return ans