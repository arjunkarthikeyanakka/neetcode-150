class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid_window(x,y):
            for i in range(58):
                if x[i] and x[i]>y[i]:
                    return False
            return True
        n,m=len(s),len(t)
        if n<m:
            return ""
        freq_t=[0]*58
        freq_s=[0]*58
        for i in t:
            freq_t[ord(i)-65]+=1
        for i in range(m):
            freq_s[ord(s[i])-65]+=1
        if valid_window(freq_t,freq_s):
            return s[:m]
        ans=1e9
        str_ans=""
        for l in range(n-m+1):
            freq_s=[0]*58
            for r in range(l,n):
                freq_s[ord(s[r])-65]+=1
                if r-l+1>=m:
                    if ans>r-l+1 and valid_window(freq_t,freq_s):
                        ans=r-l+1
                        str_ans=s[l:r+1]
                        break
        return str_ans