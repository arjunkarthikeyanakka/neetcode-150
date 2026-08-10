class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,h=0,n-1
        while l<=h:
            m=(h+l)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1
        return -1