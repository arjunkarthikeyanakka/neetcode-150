# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        intuition : check at every step if the current nodes values are same and then call recursively for left and right nodes respectively and every time check if p and q are not None if both are then its fine, if only one of them then its false. time : O(n), space : O(h)
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        return self.isSameTree(p.left,q.left) and p.val==q.val and self.isSameTree(p.right,q.right)