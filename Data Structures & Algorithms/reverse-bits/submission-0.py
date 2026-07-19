class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        bits=[0]*32
        for i in range(32):
            bits[i]=1 if (1<<i)&n else 0
        bits=bits[::-1]
        for i in range(32):
            ans+=(1<<i) if bits[i] else 0
        return ans