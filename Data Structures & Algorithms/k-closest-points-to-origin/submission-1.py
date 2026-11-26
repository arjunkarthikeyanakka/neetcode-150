from heapq import heappush as hps, heappop as hp
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n=len(points)
        def dist(x,y):
            return (x**2+y**2)**0.5
        d={}
        for i in range(n):
            d[i]=dist(points[i][0],points[i][1])
        d=dict(sorted(d.items(),key=lambda x:x[1]))
        # print(d)
        return [[points[i][0],points[i][1]] for i in d][:k]