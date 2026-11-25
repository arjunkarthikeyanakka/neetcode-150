# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx,ans=0,None
        def ino(x):
            nonlocal idx, ans
            if not x or ans:
                return
            ino(x.left)
            idx+=1
            if idx==k:
                ans=x.val
                return
            ino(x.right)
        ino(root)
        return ans