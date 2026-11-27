from collections import deque,defaultdict
class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        ans=[]
        def kahn():
            nonlocal ans
            d=defaultdict(list)
            indeg=[0]*n
            for u,v in edges:
                d[v].append(u)
                indeg[u]+=1
            dq=deque([i for i in range(n) if indeg[i]==0])
            done=0
            while dq:
                top=dq.popleft()
                done+=1
                ans.append(top)
                for x in d[top]:
                    indeg[x]-=1
                    if indeg[x]==0:
                        dq.append(x)
            return done==n
        if not kahn():
            return []
        return ans