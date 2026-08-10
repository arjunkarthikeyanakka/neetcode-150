from heapq import heappush,heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        h=[]
        ans=[]
        for i in range(k):
            heappush(h,(-nums[i],i))
        ans.append(-h[0][0])
        for i in range(k,n):
            heappush(h,(-nums[i],i))
            while h[0][1]<=i-k:
                heappop(h)
            ans.append(-h[0][0])
        return ans