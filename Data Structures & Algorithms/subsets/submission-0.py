class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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