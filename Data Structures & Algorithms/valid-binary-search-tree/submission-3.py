# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        intuition: inorder traversal of BST must yield sorted values
        '''
        num=float('-inf')
        def ino(x):
            nonlocal num
            if not x:
                return 
            ino(x.left)
            if num>=x.val:
                num=float('inf')
                return 
            else:
                num=x.val
            ino(x.right)
        ino(root)
        return num!=float('inf')