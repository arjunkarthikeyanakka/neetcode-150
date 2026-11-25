# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            l=len(q)
            for i in range(l):
                el=q.popleft()
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
                if i==l-1:
                    ans.append(el.val)
        return ans