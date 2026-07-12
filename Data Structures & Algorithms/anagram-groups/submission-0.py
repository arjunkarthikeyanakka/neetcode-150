class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def are_anagrams(s,t):
            if len(s)!=len(t):
                return False
            length=len(s)
            l,p=[0]*26,[0]*26
            for i in range(length):
                l[ord(s[i])-97]+=1
                p[ord(t[i])-97]+=1
            for i in range(26):
                if l[i]!=p[i]:
                    return False
            return True
        # 1. bruteforce T = O(m^2*n) , S = O(m)
        n=len(strs)
        ans=[]
        vis=set()
        for i in range(n):
            if i not in vis:
                curr=[strs[i]]
                vis.add(i)
                for j in range(i+1,n):
                    if are_anagrams(strs[i],strs[j]):
                        curr.append(strs[j])
                        vis.add(j)
                ans.append(curr)
        return ans