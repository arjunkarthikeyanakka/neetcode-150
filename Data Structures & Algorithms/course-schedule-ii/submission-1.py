'''
intuition: same as Course Schedule I. Edge is prereq -> course. Kahn's algorithm:
start with indegree-0 courses, pop one, append it to the order, decrement its
dependents' indegree, queue any that hit 0. The pop order is a valid topological order.
If fewer than n courses get popped, a cycle exists, so return [].
time: O(V+E), space: O(V+E)
'''
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
            while dq:
                top=dq.popleft()
                ans.append(top)
                for x in d[top]:
                    indeg[x]-=1
                    if indeg[x]==0:
                        dq.append(x)
            return ans if len(ans)==n else []
        
        return kahn()