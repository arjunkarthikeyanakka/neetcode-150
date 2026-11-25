# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        intuition: check if abs diff of ht of left and ht of right is >1 then the tree is imbalanced.
        time : O(n), space : O(h)
        '''
        flag=True
        if not root:
            return flag
        def h(x):
            nonlocal flag
            if not x:
                return 0
            l,r=h(x.left),h(x.right)
            if abs(l-r)>1:
                print(l,r,x.val)
                flag=False
            return 1+max(l,r)
        h(root)
        return flag