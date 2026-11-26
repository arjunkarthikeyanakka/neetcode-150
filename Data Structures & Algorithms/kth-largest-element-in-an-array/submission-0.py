from heapq import heappush as hps, heappop as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        h=[]
        for i in nums:
            hps(h,i)
            if len(h)==k+1:
                hp(h)
            # print(h)
        return h[0]