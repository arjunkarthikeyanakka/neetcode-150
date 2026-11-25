# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        intuition: just like doing bin search since this is a BST, you can just travel down the tree and see if both p and q are falling on one side then go there, if they both do not fall on same side, then the current root is the LCA... time : O(h), space : O(1)
        '''
        while root:
            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root