class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def helper(used=[False]*n,curr=[]):
            if len(curr)==n:
                ans.append(curr)
                return
            for i in range(n):
                if not used[i]:
                    used[i]=True
                    helper(used,curr+[nums[i]])
                    used[i]=False
        helper()
        return ans