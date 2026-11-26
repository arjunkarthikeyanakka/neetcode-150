class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        intuition: everytime you pick the elements that are not picked already, for that you maintain a bool arr, and each iteration, you toggle the picked value for an element and call helper. time : O(n*n!), space : O(n!*n)
        '''
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