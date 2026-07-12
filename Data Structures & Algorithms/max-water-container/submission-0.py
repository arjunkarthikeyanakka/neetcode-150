class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        ans=0
        while l<r:
            ans=max(ans,(r-l)*(min(nums[l],nums[r])))
            if nums[l]<=nums[r]:
                l+=1
            else:
                r-=1
        return ans