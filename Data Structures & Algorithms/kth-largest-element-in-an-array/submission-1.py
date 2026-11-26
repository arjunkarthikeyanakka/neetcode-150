from heapq import heappush as hps, heappop as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        min heap of size k, top will be the answer after adding all elements.
        time: O(nlogk), space : O(k)
        '''
        n=len(nums)
        h=[]
        for i in nums:
            hps(h,i)
            if len(h)==k+1:
                hp(h)
        return h[0]