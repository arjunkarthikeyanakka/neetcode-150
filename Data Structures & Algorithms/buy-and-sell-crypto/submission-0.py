class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window, T = O(N), S = O(1)
        # you slide through the array, update the min as you go through and maximize your difference 
        # of curr el - global min at every index.
        n=len(prices)
        if n==1:
            return 0
        ans=0
        curr=prices[0]
        for i in range(1,n):
            curr=min(curr,prices[i])
            ans=max(ans,prices[i]-curr)
        return ans