from bisect import bisect_left as bl
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        vis=set()
        for i in range(n-2):
            k=-nums[i]
            l,r=i+1,n-1
            while l<r:
                if nums[l]+nums[r]==k:
                    curr=[nums[i],nums[l],nums[r]]
                    if tuple(curr) not in vis:
                        ans.append(curr)
                    vis.add(tuple(curr))
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<k:
                    l+=1
                else:
                    r-=1
        return ans