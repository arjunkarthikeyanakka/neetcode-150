class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        intuition: you need to record everytime your curr str reaches len of 2n, every other time, you need to add open par if open is less than n and close if its less than open, we give priority to open, because we cant have balanced parantheses if we have close more than open at any stage. 
        Time: O(4ⁿ/√n)

The number of valid strings is the nth Catalan number, Cₙ ≈ 4ⁿ/(n^1.5).
Each result is a string of length 2n, so building/copying costs O(n).
Total: Cₙ · n ≈ 4ⁿ/√n.
Pruning means you never explore dead branches, so the recursion tree has roughly O(Cₙ · n) nodes, not 2²ⁿ.

Space: O(n) recursion depth (max 2n frames), excluding output. The curr + '(' strings add O(n) per frame, so strictly O(n²) if you count them. Most people say O(n).
        '''
        ans=[]
        def helper(curr='',op=0,close=0):
            if len(curr)==2*n:
                ans.append(curr)
                return
            if op<n:
                helper(curr+'(',op+1,close)
            if close<op: helper(curr+')',op,close+1)
        helper()
        return ans