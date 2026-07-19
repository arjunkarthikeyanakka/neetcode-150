class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        s=sum(nums)
        return (n*(n+1))//2-s