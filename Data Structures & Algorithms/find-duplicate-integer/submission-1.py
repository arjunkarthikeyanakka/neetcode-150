class Node:
    def __init__(self, x: int, next: 'Node' = None):
        self.val = int(x)
        self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            j=abs(nums[i])-1
            if nums[j]<0:
                return j+1
            nums[j]*=-1
        return n