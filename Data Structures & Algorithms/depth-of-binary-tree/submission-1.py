# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        intuition: if current node isnt none that means the depth is atleast 1, and you take the max of both left and right subtrees depth which are calc the same way as it is being for this node.
        Time : O(N) each node visited once
        Space : O(N) if tree is skewed, or else O(logN) 
        '''
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1