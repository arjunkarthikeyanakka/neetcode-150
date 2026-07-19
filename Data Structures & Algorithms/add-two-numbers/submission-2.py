# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        T = O(n+m) , S = O(1) aux
        just like how you do manual addition, use carry variable.
        '''
        carry=0
        i,j=l1,l2
        th=ListNode(0)
        h=th
        while i or j or carry:
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
        return h.next
        