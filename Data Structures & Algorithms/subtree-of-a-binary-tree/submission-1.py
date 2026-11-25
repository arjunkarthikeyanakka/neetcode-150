# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        intuition: at every node of root check for similarity, since you will be starting with value equality you will quickly stop checking when its not at the right place. time : O(n.m) worst case : check runs at up to n nodes and each call costs up to m. space : O(h1+h2)
        '''
        def check(x,y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val==y.val and check(x.left,y.left) and check(x.right,y.right) 
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return check(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
