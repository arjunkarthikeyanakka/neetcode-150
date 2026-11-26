'''
DSU template:
intuition: add edges one by one with union-find. If an edge's endpoints already share
a root, they're already connected, so this edge closes the cycle. Return it.
time: O(n * α(n)) ≈ O(n), space: O(n)
'''
class DSU:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.size=[1]*(n+1)
    def find(self,u):
        while self.parent[u]!=u:
            self.parent[u]=self.parent[self.parent[u]]
            u=self.parent[u]
        return u
    def union(self,u,v):
        pu,pv=self.find(u),self.find(v)
        if pu==pv:
            return False
        if self.size[pu]>self.size[pv]:
            pu,pv=pv,pu
        self.parent[pu]=pv
        self.size[pv]+=self.size[pu]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        dsu=DSU(n)
        for x,y in edges:
            if not dsu.union(x,y):
                return [x,y]
