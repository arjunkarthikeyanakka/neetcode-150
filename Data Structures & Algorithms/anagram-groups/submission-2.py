from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def are_anagrams(s,t):
        #     if len(s)!=len(t):
        #         return False
        #     length=len(s)
        #     l,p=[0]*26,[0]*26
        #     for i in range(length):
        #         l[ord(s[i])-97]+=1
        #         p[ord(t[i])-97]+=1
        #     for i in range(26):
        #         if l[i]!=p[i]:
        #             return False
        #     return True
        # 1. bruteforce T = O(m^2*n) , S = O(m*n)
        # n=len(strs)
        # ans=[]
        # vis=set()
        # for i in range(n):
        #     if i not in vis:
        #         curr=[strs[i]]
        #         vis.add(i)
        #         for j in range(i+1,n):
        #             if are_anagrams(strs[i],strs[j]):
        #                 curr.append(strs[j])
        #                 vis.add(j)
        #         ans.append(curr)
        # return ans

        # 2. hashtable T = O(m*n), S = O(m) 
        # need to use a tuple as dictionary key as only immutable ds can be used as dict keys
        # since l's size is fixed (26), so we have total memory to O(m) where m is len(strs)
        def helper(s):
            l=[0]*26
            for i in range(len(s)):
                l[ord(s[i])-97]+=1
            ret=tuple(l)
            return ret

        d=defaultdict(list)
        for i in range(len(strs)):
            d[helper(strs[i])].append(i)
        ans=[]
        for i in d:
            curr=[]
            for j in d[i]:
                curr.append(strs[j])
            ans.append(curr)
        return ans












