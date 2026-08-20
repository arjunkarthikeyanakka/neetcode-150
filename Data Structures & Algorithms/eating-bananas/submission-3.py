class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Optimal solution : T = O(nlogm), S = O(1) aux
        You have to do bin search in the range 1 to max(piles) and you can keep minimising it 
        until left>right.
        '''
        def works(k):
            c=0
            for i in piles:
                c+=max(1,i//k+(1 if i%k else 0))
            return c
        n=len(piles)
        ans=1e9
        if n==h:
            return max(piles)
        left,right=1,max(piles)
        while left<=right:
            mid=left+(right-left)//2
            k=works(mid)
            # print(left,mid,right,k)
            if k<=h:
                ans=min(ans,mid)
                right=mid-1
            else:
                left=mid+1

        return ans