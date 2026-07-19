class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Approach is great, i was doing the same but i was checking the polarity 
        on the second pass of the full array, that will not work if the duplicate is
        of odd multiplicity, to make it work, we will check for negative polarity 
        in single pass, we take absolute of current number, where we will get idx to
        reverse polarity, and we check on fly if the index where we have to flip polarity
        is already negative, then we have our answer.
        T = O(n) , S = O(1)
        Note : took 35 minutes but finally took hint from gemini that i had do everything
        in single pass not 2 passes. This is the optimal solution.
        '''
        '''
        n=len(nums)
        for i in range(n):
            j=abs(nums[i])-1
            if nums[j]<0:
                return j+1
            nums[j]*=-1
        return n
        '''

        '''
        this is another approach, although not as pure as the above one.
        '''
        n=len(nums)
        bits = [0]*32
        for i in range(32):
            for j in nums:
                bits[i]+=1 if (1<<i)&j else 0
        for i in range(32):
            for j in range(1,n):
                bits[i]-=1 if (1<<i)&j else 0
       
        ans=0
        for i in range(32):
            if bits[i]>0:
                ans+=(1<<i)
        return ans



