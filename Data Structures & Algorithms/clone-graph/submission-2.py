"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        intuition: map each original node to its clone. DFS: clone a node before visiting
        its neighbors, so a cycle finds the existing clone instead of recursing forever.
        Then append each neighbor's clone to the current clone's neighbors.
        time: O(V+E), space: O(V)
        '''
        d=defaultdict(Node)
        def dfs(curr_node):
            copy_par=d[curr_node]
            for neighbor in curr_node.neighbors:
                if neighbor not in d:
                    d[neighbor]=Node(neighbor.val)
                    dfs(neighbor)
                copy_par.neighbors.append(d[neighbor])
        if not node:
            return None    
        d[node]=Node(node.val)
        dfs(node)
        return d[node]
