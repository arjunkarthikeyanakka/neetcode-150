from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. brute force T = O(n^2), S = O(1)
        # n=len(nums)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        
        # 2. hashmap T = O(n), S = O(1)
        d=defaultdict(int)
        for idx,i in enumerate(nums):
            if d.get(i,-1)+1:
                return [d[i],idx]
            d[target-i]=idx
        