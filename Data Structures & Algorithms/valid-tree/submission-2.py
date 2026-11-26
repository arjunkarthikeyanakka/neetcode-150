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