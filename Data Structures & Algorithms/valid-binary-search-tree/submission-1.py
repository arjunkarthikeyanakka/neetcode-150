# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(x,l,h):
            if not x:
                return True
            if not(l<x.val<h):
                return False
            return valid(x.left,l,x.val) and valid(x.right,x.val, h)
        return valid(root,float('-inf'),float('inf'))