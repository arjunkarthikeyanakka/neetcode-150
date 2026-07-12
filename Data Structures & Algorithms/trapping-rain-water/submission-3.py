class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0 
        ans=0
        start,end=0,n-1
        for i in range(n):
            if nums[i]:
                start=i
                break
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                end=i+1
                break
        m=max(nums)
        d=dict(sorted(Counter(nums).items(),key=lambda x:x[0],reverse=1))
        if d[m]==1:
            it=iter(d)
            next(it)
            m=next(it)
        for i in range(start,end+1):
            nums[i]=min(nums[i],m)
        # print(nums)
        i=start
        stack=[nums[i]]
        ans=0
        first=nums[i]
        i+=1
        while i<end:
            if nums[i]<first:
                stack.append(nums[i])
            else:
                # print(stack)
                curr=first*len(stack)-sum(stack)
                ans+=curr
                first=nums[i]
                stack=[first]
            i+=1
        i=min(end,n-1)
        # print('end',stack,nums[i])
        if stack!=[]:
            first=min(nums[i],first)
            for j in stack:
                ans+=first-(min(first,j))
        return ans
