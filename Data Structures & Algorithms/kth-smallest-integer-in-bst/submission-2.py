# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Making use of BST ordering, we set 2 nonlocal var to count idx and then store the kth element.
        The extra check of ans is not None is to early exit when you find the kth element.
        time : O(h+k) ideally, O(n) worst case
        space : O(h) recursion stack.
        '''
        idx,ans=0,None
        def ino(x):
            nonlocal idx, ans
            if not x or ans is not None:
                return
            ino(x.left)
            idx+=1
            if idx==k:
                ans=x.val
                return
            ino(x.right)
        ino(root)
        return ans