from bisect import bisect_left as bl
class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            idx=bl(nums,k-nums[i],i+1,n)
            if idx>=0 and idx<n and nums[i]+nums[idx]==k:
                return [i+1,idx+1]