class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        arr=[-1]*95
        ans=0
        start=0
        for idx,i in enumerate(s):
            j=ord(i)-32
            if arr[j]+1:
                ans=max(ans,idx-start)
                start=max(start,arr[j]+1)
            arr[j]=idx
        print(start,ans)
        return max(ans,len(s)-start)