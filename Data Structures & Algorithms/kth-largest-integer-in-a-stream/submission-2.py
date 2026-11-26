from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        for i in nums:
            heappush(self.heap,i)
            while len(self.heap)>k:
                heappop(self.heap)
        # print(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap,val)
        while len(self.heap)>self.k:
            heappop(self.heap)
        # print(self.heap)
        return self.heap[0]