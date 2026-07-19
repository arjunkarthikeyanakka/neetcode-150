"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        th=Node(0)
        h=th
        temp=head
        idx=0
        rd_idx,b=defaultdict(int),[]
        while temp:
            th.next=Node(temp.val,None,None)
            th=th.next
            rd_idx[temp]=idx
            b.append(th)
            idx+=1
            temp=temp.next
        x,y=h.next,head
        while x:
            # print(y.val,rd_idx[y.random])
            x.random=b[rd_idx[y.random]] if y.random else None
            x=x.next
            y=y.next
        return h.next