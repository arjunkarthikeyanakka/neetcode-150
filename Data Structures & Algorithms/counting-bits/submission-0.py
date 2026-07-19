class Solution:
    def countBits(self, n: int) -> List[int]:
        def bits(x):
            c=0
            for i in range(32):
                c+=1 if x&(1<<i) else 0
            return c
        ans=[0]*(n+1)
        for i in range(1,n+1):
            ans[i]=bits(i)
        return ans