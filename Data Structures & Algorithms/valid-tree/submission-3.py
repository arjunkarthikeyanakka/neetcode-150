class DSU:
    def __init__(self,n):
        self.par=list(range(n))
        self.size=[1]*n
    def find(self,x):
        while self.par[x]!=x:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x
    def union(self,u,v):
        pu,pv=self.find(u),self.find(v)
        if pu==pv:
            return False
        if self.size[pu]>=self.size[pv]:
            pu,pv=pv,pu
        self.size[pv]+=self.size[pu]
        self.par[pu]=pv
        return True

class Solution:
    '''
    intuition: a valid tree is connected with no cycle. Exactly n-1 edges rules out
    "too many" (forced cycle) and "too few" (disconnected). With n-1 edges, no cycle
    implies connected, so use DSU: if an edge joins two already-connected nodes,
    it's a cycle, return False.
    time: O(n * α(n)), space: O(n)
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        E=len(edges)
        if E!=n-1:
            return False
        dsu=DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        return True