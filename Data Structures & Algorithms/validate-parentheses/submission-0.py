class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in d:
                if st and st[-1] == d[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

        return True if not st else False