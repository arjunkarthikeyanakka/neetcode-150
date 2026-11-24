# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):
        if not root or (not root.left and not root.right):
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        time : O(n^2) worst case - skewed tree, space : O(h) recursive stack
        '''
        if not root:
            return 0
        return max((1 if root.left else 0)+(1 if root.right else 0)+self.height(root.left)+self.height(root.right),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))