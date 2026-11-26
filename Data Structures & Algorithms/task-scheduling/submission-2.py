from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l=len(tasks)
        if n==0:
            return l
        d=Counter(tasks)
        f=d.most_common(1)[0][1]
        print(f)
        g=0
        for i in d:
            if d[i]==f:
                g+=1
        return max(l,min(f*(n+1),(n+1)*(f-1)+g))