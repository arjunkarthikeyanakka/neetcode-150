'''
intuition: courses are nodes, "prereq -> course" are directed edges. All courses can
be finished iff the graph is a DAG, i.e. a topological order exists.
DSU can't be used: it ignores direction, so it flags harmless edges like
A->B, B->C, A->C as a cycle.
Kahn's algorithm: indegree = number of unmet prerequisites. Start with all indegree-0
nodes (no prerequisites). Process one: it's done, so decrement its neighbors' indegree;
any that reach 0 are now unblocked and join the queue. Nodes on a cycle each wait on
another cycle node, so their indegree never hits 0 and they're never processed.
So done == n  <=>  no cycle.
time: O(V+E), space: O(V+E)
'''
from collections import deque,defaultdict
class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        d=defaultdict(list)
        indeg=[0]*n
        for u,v in edges:
            d[u].append(v)
            indeg[v]+=1
        dq=deque([i for i in range(n) if indeg[i]==0])
        done=0
        while dq:
            top=dq.popleft()
            done+=1
            for x in d[top]:
                indeg[x]-=1
                if indeg[x]==0:
                    dq.append(x)
        return done==n
