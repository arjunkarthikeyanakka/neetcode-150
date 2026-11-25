# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        bfs_q=deque()
        bfs_q.appendleft(root)
        while bfs_q:
            curr=[]
            l=len(bfs_q)
            for _ in range(l):
                top=bfs_q.pop()
                curr.append(top.val)
                if top.left:
                    bfs_q.appendleft(top.left)
                if top.right:
                    bfs_q.appendleft(top.right)
            ans.append(curr)
        return ans