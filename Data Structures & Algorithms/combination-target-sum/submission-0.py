class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def helper(idx,curr=[],s=0):
            if idx>=n or s>target:
                return
            if s==target:
                ans.append(curr)
                return
            helper(idx,curr+[nums[idx]],s+nums[idx])
            helper(idx+1,curr,s)
        helper(0)
        return ans