class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        intuition: for each element, make one decision: include it or skip it.
        Recursing on both branches builds a binary decision tree with 2^n leaves,
        and each leaf is one subset.
        time: O(n * 2^n)  (2^n subsets, each built/copied in O(n))
        space: O(n) recursion depth, excluding output
        '''
        n=len(nums)
        ans=[]
        def helper(i,curr=[]):
            nonlocal n, ans
            if i==n:
                ans.append(curr)
                return 
            helper(i+1,curr+[nums[i]])
            helper(i+1,curr)
        helper(0)
        return ans