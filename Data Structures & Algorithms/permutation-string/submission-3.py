class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            this is a lot easier compared to the prev problem.
            T = O(n+m), S = O(1)
            Now, the idea is that the window will be of size n
            n = len(s1), we compare both freq arrays where we 
            are interested (only characters that s1 has)
            if they are not all equal then its not a permutation
            ofcourse our solution is optimal because we can 
            without fear use two freq arrays to check them at every
            character of s2 as they are fixed size 26.
        '''
        def same(x,y):
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