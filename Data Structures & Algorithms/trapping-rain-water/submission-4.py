class Solution:
    def trap(self, nums: List[int]) -> int:
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
