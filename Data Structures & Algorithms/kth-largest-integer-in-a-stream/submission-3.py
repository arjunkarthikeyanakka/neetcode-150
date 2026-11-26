from heapq import heappush, heappop
class KthLargest:
    '''
    intuition: keep only the k largest values seen so far in a min heap. The root is the
    smallest of those k, which is exactly the kth largest. Anything popped is beaten by
    k other values, so it can never be the answer again.
    time: constructor O(n log k), add O(log k)
    space: O(k)
    '''
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        for i in nums:
            heappush(self.heap,i)
            while len(self.heap)>k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap,val)
        while len(self.heap)>self.k:
            heappop(self.heap)
        return self.heap[0]