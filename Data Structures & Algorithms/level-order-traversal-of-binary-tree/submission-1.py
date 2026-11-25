# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        intuition: do a bfs... time : O(n), space: O(n), imp to use append and popleft, as pop and insert are O(n) because every element shifts...
        '''
        if not root:
            return []
        ans=[]
        bfs_q=deque([root])
        while bfs_q:
            curr=[]
            l=len(bfs_q)
            for _ in range(l):
                top=bfs_q.popleft()
                curr.append(top.val)
                if top.left:
                    bfs_q.append(top.left)
                if top.right:
                    bfs_q.append(top.right)
            ans.append(curr)
        return ans