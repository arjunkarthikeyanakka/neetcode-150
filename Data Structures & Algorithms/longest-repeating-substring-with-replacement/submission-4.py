class Solution:
    def characterReplacement(self, t: str, k: int) -> int:
        n=len(t)
        freq=[0]*26
        l,r=0,1
        freq[ord(t[0])-65]+=1
        ans=1
        while r<n:
            freq[ord(t[r])-65]+=1
            rep=r-l-max(freq)+1
            if rep>k:
                freq[ord(t[l])-65]-=1
                l+=1
            r+=1
            ans=max(ans,r-l)
        return max(ans,r-l)