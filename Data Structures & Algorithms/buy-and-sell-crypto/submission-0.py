class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1:
            return 0
        ans=0
        curr=prices[0]
        for i in range(1,n):
            curr=min(curr,prices[i])
            ans=max(ans,prices[i]-curr)
        return ans