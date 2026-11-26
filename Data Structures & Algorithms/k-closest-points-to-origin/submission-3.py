from heapq import heappush as hps, heappop as hp
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        using max heap 
        Time: O(n log k)
        Space: O(k)
        '''
        n=len(points)
        def dist(x,y):
            return (x**2+y**2)**0.5
        h=[]
        for i in range(n):
            hps(h,(-dist(points[i][0],points[i][1]),i))
        while len(h)>k:
            hp(h)
        ans=[]
        while h:
            el=hp(h)
            ans.append(points[el[1]])
        return ans