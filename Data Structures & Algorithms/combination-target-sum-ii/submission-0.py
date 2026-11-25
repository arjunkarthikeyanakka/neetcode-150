class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def helper(idx,curr=[],s=0):
            if idx==n or s>=target:
                if s==target: ans.append(curr)
                return
            helper(idx+1,curr+[nums[idx]],s+nums[idx])
            while idx+1<n and nums[idx+1]==nums[idx]:
                idx+=1
            helper(idx+1,curr,s)
        nums.sort()
        helper(0)
        return ans