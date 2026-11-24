# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        intuition : To invert a tree, swap the two children at every node. That's it. The recursion just visits every node and does that one swap. 
        Time: O(n), each node visited once.
Space: O(h) recursion stack. O(log n) balanced, O(n) for a skewed tree.
        '''
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root