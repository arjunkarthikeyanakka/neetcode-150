from heapq import heappush as hps, heappop as hp, heapify as hf
class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        heap=[]
        for i in nums:
            hps(heap,-i)
        while len(heap)>1:
            x=hp(heap)
            y=hp(heap)
            if x!=y:
                hps(heap,-1*abs(x-y))
        return -heap[0] if len(heap) else 0