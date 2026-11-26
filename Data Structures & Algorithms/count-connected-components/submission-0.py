from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp=0
        vis=set()
        def dfs(x):
            if x in vis:
                return
            vis.add(x)
            for y in d[x]:
                if y not in vis:
                    dfs(y)
        d=defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        for i in range(n):
            if i not in vis:
                dfs(i)
                comp+=1
        return comp