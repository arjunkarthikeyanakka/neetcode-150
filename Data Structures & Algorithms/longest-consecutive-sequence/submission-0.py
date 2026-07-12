class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1:
            return n
        # brute force - sort T = O(nlogn+n), S = O(1)
        nums.sort()
        ans,prev=0,nums[0]
        curr=1
        for i in range(1,n):
            if nums[i]-1==prev:
                curr+=1
            elif nums[i]==prev:
                continue
            else:
                ans=max(ans,curr)
                curr=1
            prev=nums[i]
        return max(ans,curr)