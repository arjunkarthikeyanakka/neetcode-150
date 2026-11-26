from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        intuition: the most frequent task sets the schedule: (f-1) blocks of width n+1 will definitely be there, so we have to solve how many slots we'll have to fill in the last box of n+1 slots, until the last box we will only be left with most frequent elements, so we find many elements of max freq exist = g, and we add g to it.
        time: O(m), space: O(1) (26 letters)
        '''
        l=len(tasks)
        d=Counter(tasks)
        f=d.most_common(1)[0][1]
        g=0
        for i in d:
            if d[i]==f:
                g+=1
        return max(l,(n+1)*(f-1)+g)