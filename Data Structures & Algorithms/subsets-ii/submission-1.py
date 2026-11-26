class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        kind of similar to comb sum 2, since there is no specific order in each nested answer, we can sort nums and skip dupes. That is all, time: O(n*2^n), space : O(n)
        '''
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