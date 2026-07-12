class Solution:
    def trap(self, nums: List[int]) -> int:
        # brute force : T = O(NlogN), S = O(N)
        '''
            the idea is to start at a peak and end at a peak, so we have proper boundaries
            then we change the nums array if in those boundaries the max occurs only once, we normalize it to second max
            then we traverse from start to end and using a stack we sum all elements and subtract from bucket height to get water vol
            if the stack is non empty even after reaching end, that means the left wall height is higher than anything that comes after it
            so you can simply do a diff of len stack * left wall height - sum of stack elems. 
            
            But there is even a better way, embarrassingly there is no need to optimize this far, we can just use 2 pointers.
        '''
        '''
        n=len(nums)
        if n<3:
            return 0 
        ans=0
        start,end=0,n-1
        for i in range(n):
            if nums[i] and (i+1<n and nums[i]>nums[i+1]):
                start=i
                break
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                end=i+1
                break
        m=max(nums)
        # print(start,end,'start,end')
        d=dict(sorted(Counter(nums).items(),key=lambda x:x[0],reverse=1))
        if d[m]==1:
            it=iter(d)
            next(it)
            m=next(it)
        for i in range(start,end+1):
            nums[i]=min(nums[i],m)
        mx_nums=[i for i in nums]
        for i in range(n-2,-1,-1):
            mx_nums[i]=max(mx_nums[i],mx_nums[i+1])
        # print(nums,mx_nums)
        i=start
        stack=[nums[i]]
        ans=0
        first=nums[i]
        i+=1
        while i<=end:
            if nums[i]<=first:
                stack.append(nums[i])
            else:
                curr=first*len(stack)-sum(stack)
                # print(stack,curr)
                ans+=curr
                if i+1<n:
                    first=min(nums[i],mx_nums[i+1])
                else:
                    first=nums[i]
                stack=[first]
            i+=1
        i=min(end,n-1)
        # print('end',stack,nums[i])
        first=nums[i]
        while stack:
            while stack:
                el=stack.pop(-1)
                if el>first:
                    first=el
                    break
                ans+=(first-el)
                    
        return ans
        '''
        
        # 2. optimal : T = O(N), S = O(1)
        # 2 pointer approach. No need to check for start, end, walls and everything is taken care of the max left and right variables
        # you choose to focus on what side each time.
        n=len(nums)
        if n<3:
            return 0 
        ans=0
        l,r=0,n-1
        ml,mr=nums[0],nums[-1]
        while l<r:
            if nums[l]<nums[r]:
                # index l is the wall right now, because that is the min of both
                ml=max(ml,nums[l])
                ans+=ml-nums[l]
                l+=1
            else:
                # index r is the wall as it is <=l
                mr=max(mr,nums[r])
                ans+=mr-nums[r]
                r-=1
        return ans
