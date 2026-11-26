class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def helper(idx,curr=[]):
            if idx==n:
                ans.append(curr)
                return 
            helper(idx+1,curr+[nums[idx]])
            while idx+1<n and nums[idx]==nums[idx+1]:
                idx+=1    
            helper(idx+1,curr)
        nums.sort()
        helper(0)
        return ans