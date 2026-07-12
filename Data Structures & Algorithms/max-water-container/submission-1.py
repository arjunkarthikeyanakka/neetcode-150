class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        ans=0
        while l<r:
            curr=(r-l)*(nums[l])
            if nums[l]<=nums[r]:
                l+=1
            else:
                curr=(r-l)*(nums[r])
                r-=1
            ans=max(ans,curr)
        return ans