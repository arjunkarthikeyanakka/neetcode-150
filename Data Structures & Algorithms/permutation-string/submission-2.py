class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def same(x,y):
            # print(freq2)
            for i in range(26):
                if x[i] and x[i]!=y[i]:
                    return False
            return True

        n,m=len(s1),len(s2)
        if n>m:
            return False
        freq1=[0]*26
        for i in s1:
            freq1[ord(i)-97]+=1
        freq2=[0]*26
        for i in range(n):
            freq2[ord(s2[i])-97]+=1
        if same(freq1,freq2):
            return True
        for i in range(n,m):
            freq2[ord(s2[i-n])-97]-=1
            freq2[ord(s2[i])-97]+=1
            if same(freq1,freq2):
                return True
        return False