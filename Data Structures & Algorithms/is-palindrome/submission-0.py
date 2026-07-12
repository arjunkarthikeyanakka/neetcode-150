import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(i for i in s if i.isalnum()).lower()
        n=len(s)
        for i in range(n//2):
            if s[i]!=s[n-i-1]:
                return False
        return True