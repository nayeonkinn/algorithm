# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m = ListNode()
        head = m

        while l1 and l2:
            if l1.val < l2.val:
                m.next = l1
                l1 = l1.next
                m = m.next
            else:
                m.next = l2
                l2 = l2.next
                m = m.next

        if l2:
            l1 = l2
        while l1:
            m.next = l1
            m = m.next
            l1 = l1.next

        return head.next