import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force, T = O(n), S = O(n)
        # s="".join(i for i in s if i.isalnum()).lower()
        # n=len(s)
        # for i in range(n//2):
        #     if s[i]!=s[n-i-1]:
        #         return False
        # return True

        # optimal, T = O(n), S = O(1)
        n=len(s)
        i,j=0,n-1
        while i<n and j>=0:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()==s[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
            elif not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
        return True
