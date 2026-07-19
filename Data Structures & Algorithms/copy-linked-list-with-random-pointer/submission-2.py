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
        # optimal time wise, but space can be optimized even more. 
        # T = O(n), S = O(n)
        '''
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
            x.random=b[rd_idx[y.random]] if y.random else None
            x=x.next
            y=y.next
        return h.next
        '''

        # okay so this technique is called Three-Step In-Place Interweaving Trick
        # basically, you will create copies of each node right beside it, so its easy 
        # for you to stitch the random nodes of the copied nodes as they will be right beside 
        # the actual random nodes, you dont have to search for them. Only special case is
        # random being a null. 
        # T = O(n), S = O(1) auxiliary space. This is the most optimal solution
        # considering both time and space wise.
        if head is None:
            return head
        th=Node(0)
        h=th
        temp=head
        while temp:
            temp.next=Node(temp.val,temp.next,None)
            temp=temp.next.next
        temp=head
        while temp and temp.next:
            copy_node=temp.next
            copy_node.random=temp.random.next if temp.random else temp.random
            temp=temp.next.next
        temp=head
        th=temp.next
        while temp:
            copy_node=temp.next
            nn=temp.next.next
            temp.next=nn
            if copy_node.next and copy_node.next.next:
                copy_node.next=nn.next
            temp=nn
        
        return th
