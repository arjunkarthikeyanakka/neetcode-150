class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1:
            return n
        # brute force - sort T = O(nlogn+n), S = O(1)
        # nums.sort()
        # ans,prev=0,nums[0]
        # curr=1
        # for i in range(1,n):
        #     if nums[i]-1==prev:
        #         curr+=1
        #     elif nums[i]==prev:
        #         continue
        #     else:
        #         ans=max(ans,curr)
        #         curr=1
        #     prev=nums[i]
        # return max(ans,curr)

        # optimal approach, T = O(n), S=O(n)
        # idea is to maintain a set to see if there is no predecessor (nums[i]-1) in nums, so we can start 
        # our sequence from there and a while loop runs to get length of our consecutive inc subseq.
        vis=set(nums)
        curr,ans=0,0
        for i in range(n):
            if nums[i]-1 in vis:
                continue
            x=nums[i]
            while x in vis:
                x+=1
                curr+=1
            ans=max(ans,curr)
            curr=0
        return max(ans,curr)


