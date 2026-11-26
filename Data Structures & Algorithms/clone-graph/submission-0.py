"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d=defaultdict(Node)
        vis=set()
        def dfs(curr_node):
            nonlocal d
            if curr_node in vis:
                return
            vis.add(curr_node)
            copy_par=d[curr_node]
            for neighbor in curr_node.neighbors:
                if neighbor not in vis:
                    d[neighbor]=Node(neighbor.val)
                    dfs(neighbor)
                copy_par.neighbors.append(d[neighbor])
        if not node:
            return None    
        d[node]=Node(1)
        dfs(node)
        return d[node]
