from bisect import bisect_left as bl
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(n-2):
            if i and nums[i]==nums[i-1]:
                continue
            k=-nums[i]
            l,r=i+1,n-1
            while l<r:
                if nums[l]+nums[r]==k:
                    curr=[nums[i],nums[l],nums[r]]
                    ans.append(curr)
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]<k:
                    l+=1
                else:
                    r-=1
        return ans