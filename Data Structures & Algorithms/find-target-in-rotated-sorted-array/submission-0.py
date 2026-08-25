class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left,right=0,n-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        pivot=left
        l1,r1,l2,r2=0,left-1,left,n-1
        while l1<=r1:
            m1=l1+(r1-l1)//2
            if nums[m1]==target:
                return m1
            elif nums[m1]<target:
                l1=m1+1
            else:
                r1=m1-1
        while l2<=r2:
            m2=l2+(r2-l2)//2
            if nums[m2]==target:
                return m2
            elif nums[m2]<target:
                l2=m2+1
            else:
                r2=m2-1
        return -1