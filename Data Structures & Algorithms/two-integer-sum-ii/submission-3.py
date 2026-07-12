from bisect import bisect_left as bl
class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        # brute force, T = O(nlogn), S = O(1)
        n=len(nums)
        # for i in range(n):
        #     idx=bl(nums,k-nums[i],i+1,n)
        #     if idx>=0 and idx<n and nums[i]+nums[idx]==k:
        #         return [i+1,idx+1]

        # optimal, T = O(n), S = O(1)
        left,right=0,n-1
        while left<right:
            if nums[left]+nums[right]==k:
                return [left+1,right+1]
            elif nums[left]+nums[right]<k:
                left+=1
            else:
                right-=1