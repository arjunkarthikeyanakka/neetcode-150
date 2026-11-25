class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            intuition: for each number, either take it (and stay, since reuse is allowed)
            or skip it for good (move to next index). Moving only forward avoids duplicate
            permutations like [2,3] vs [3,2].
            time: O(2^(t/m)) roughly, t = target, m = min(nums); branching depth is at most t/m
            space: O(t/m) recursion depth, excluding output
        '''
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