class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            The idea is to find the pivot where current element is lower than the one before it.
            To find this, compare mid element with right, if the mid element is higher then the 
            min is towards right, else move to the left. Imp thing is while condition is left<right
            and left=mid+1 and right=mid
        '''
        if nums[0]<nums[-1]:
            return nums[0]
        n=len(nums)
        ans=0
        left,right=0,n-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]
