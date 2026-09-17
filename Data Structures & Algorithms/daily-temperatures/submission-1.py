class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        '''
        Each element gets pushed once and popped at most once, so the whole scan is O(n) total capped at 2n even though it feels like nested loops, each element is only ever compared/popped once across the entire run. Remember the template as this : 
        ```
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:  # or > for increasing stack
                top = stack.pop()
                # do something with `top` using arr[i] as the "answer" for it
            stack.append(i)
        ```

        T=O(n), S=O(n)
        '''
        n=len(t)
        stack=[]
        ans=[0]*n
        for idx,val in enumerate(t):
            while stack and val>t[stack[-1]]:
                j=stack.pop(-1)
                ans[j]=idx-j
            stack.append(idx)
        return ans