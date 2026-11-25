class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        intuition stays almost same as comb sum 1, just have to skip the dupes on empty curr, so the second call, is used for creating a new empty arr with idx+1 el, but if idx and idx+1 el are same, then it must have already been done before, to avoid duplicates, we skip past these same elements, to do that we need to sort the array first. Complexity: time O(2ⁿ) worst case, space O(n) recursion depth
        '''
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