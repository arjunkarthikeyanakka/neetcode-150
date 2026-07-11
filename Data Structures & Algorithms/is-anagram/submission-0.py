class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. bruteforce T = O(nlogn) , S = O(n+m)
        # l,p=sorted(list(s)),sorted(list(t))
        # return l==p
        
        # 2. using counter T = O(n+n), S = O(1) 
        # the space complexity is O(1) because its 2 dictionaries with max 26 keys
        # return Counter(s)==Counter(t)

        # 3. alphabet counter T = O(n), S = O(1) 
        if len(s)!=len(t):
            return False
        n=len(s)
        i=0
        x,y=[0]*26,[0]*26
        while i<n:
            x[ord(s[i])-97]+=1
            y[ord(t[i])-97]+=1
            i+=1
        for i in range(26):
            if x[i]!=y[i]:
                return False
        return True