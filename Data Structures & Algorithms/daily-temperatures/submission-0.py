class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n=len(t)
        stack=[]
        ans=[0]*n
        for v,i in enumerate(t):
            if stack==[]:
                stack.append(v)
            else:
                while stack and i>t[stack[-1]]:
                    j=stack.pop(-1)
                    ans[j]=v-j
                stack.append(v)
        return ans