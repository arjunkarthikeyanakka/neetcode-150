class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        for i in range(32):
            ans+=1 if (1<<i)&n else 0
        return ans