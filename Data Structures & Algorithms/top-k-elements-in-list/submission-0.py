# from heapq import heappop, heappush
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # optimal approach. T = O(n), S = O(n)
        n=len(nums)
        d=Counter(nums)
        dd=defaultdict(list)
        for i in d:
            dd[d[i]].append(i)
        ans=[]
        # traversing in reverse, helps us the extra O(N*logN) of sorting dd by keys, 
        # we need top k elements so we need to go in reverse. 
        for i in range(n,-1,-1):
            for j in dd[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans