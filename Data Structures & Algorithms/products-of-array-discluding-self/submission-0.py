class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # optimal : T = O(n), S = O(1) ***consider auxiliary space meaning it doesnt include answer array space. 
        # brute force would be having two arrays prefix and suffix which would mean O(n).
        n=len(nums)
        if n==1:
            return nums
        ans=[1 for i in nums]
        prefix=1
        for i in range(n):
            ans[i]*=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans