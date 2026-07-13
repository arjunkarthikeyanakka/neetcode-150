# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Explanation : 
T = O(N),  S = O(1)
first check the length of the list so that you can reverse
the second half and then rewire first half and second half 
nodes by running two pointers.
Better way is to run slow and fast pointers this will save 
you a full list traversal. Code is not so readable right now
but the idea is clearly explained, you wrote this within 30 
minutes without any help or recollection of older submissions 
so you can do it again!
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
	    n=0
        th=head
        while th:
            n+=1
            th=th.next
        if n<3:
            return 
        slow=head
        fast=head
        c=0
        p=head
        while c<(n+1)//2:
            c+=1
            p=fast
            fast=fast.next
        curr=fast
        prev=None
        p.next=None
        pp=curr
        while curr:
            nn=curr.next
            curr.next=prev
            prev=curr
            curr=nn
        fast=prev
        while slow and fast:
            left_next=slow.next
            right_next=fast.next
            slow.next=fast
            slow=left_next
            fast.next=slow
            fast=right_next 
        