from heapq import heappush, heappop
from collections import defaultdict
class MinStack:

    def __init__(self):
        self.st=[]
        self.h=[]
        self.c=defaultdict(int)

    def push(self, val: int) -> None:
        self.st.append(val)
        heappush(self.h,val)
        self.c[val]+=1
        # print(self.st)

    def pop(self) -> None:
        el=self.st.pop(-1)
        if self.c[el]==1:
            del self.c[el]
        else:
            self.c[el]-=1
        # print(self.st)

    def top(self) -> int:
        # print(self.st)
        return self.st[-1]

    def getMin(self) -> int:
        while self.h and self.c.get(self.h[0],0)==0:
            heappop(self.h)
        # print(self.st)
        return self.h[0] if self.h else None