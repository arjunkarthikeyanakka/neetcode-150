# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        th=head
        while th:
            th=th.next
            l+=1
        n=l-n
        if l<2:
            return None
        curr,prev=head,None
        c=0
        while c<n and curr:
            prev=curr
            curr=curr.next
            c+=1
        if not prev:
            return head.next
        prev.next=curr.next
        return head