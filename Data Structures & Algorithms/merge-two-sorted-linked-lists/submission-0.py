# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1,h2=list1,list2
        th=ListNode(0,None)
        h=ListNode(-1,None)
        h.next=th
        while h1 and h2:
            if h1.val<=h2.val:
                if not th:
                    th=h1
                else:
                    th.next=h1
                h1=h1.next
            else:
                if not th:
                    th=h2
                else:
                    th.next=h2
                h2=h2.next
            th=th.next
        while h1:
            if not th:
                th=h1
            else:
                th.next=h1
            h1=h1.next
            th=th.next

        while h2:
            if not th:
                th=h2
            else:
                th.next=h2
            h2=h2.next
            th=th.next

        return h.next.next