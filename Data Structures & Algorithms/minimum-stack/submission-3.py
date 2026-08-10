from heapq import heappush, heappop
from collections import defaultdict
class MinStack:

    def __init__(self):
        self.st=[]
        self.mn=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.mn==[]:
            self.mn.append(val)
        else:
            t=self.mn[-1]
            self.mn.append(min(t,val))

    def pop(self) -> None:
        self.st.pop(-1)
        self.mn.pop(-1)

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mn[-1]
        