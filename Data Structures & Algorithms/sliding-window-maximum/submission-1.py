from heapq import heappush,heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        T = O(nlogn), S = O(n)
        You are processing each element once, and every time you will either few deletes but one definite addition to the max heap. You dont care about the top element unless its index is out of the window range. This makes it optimal. Stale elements linger which makes worst space to be full O(n) ex: [4,3,2,1] (strictly decreasing).
        '''
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