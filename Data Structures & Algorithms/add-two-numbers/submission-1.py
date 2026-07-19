# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        i,j=l1,l2
        th=ListNode(0)
        h=th
        while i or j:
            curr=carry
            if i:
                curr+=i.val
            if j:
                curr+=j.val
            th.next=ListNode(curr%10)
            th=th.next
            carry=curr//10
            if i:
                i=i.next
            if j:
                j=j.next
        if carry:
            th.next=ListNode(1)
            th=th.next
        return h.next
        