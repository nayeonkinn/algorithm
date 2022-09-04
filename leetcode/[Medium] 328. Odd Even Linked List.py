# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o = odd = ListNode()
        e = even = ListNode()
        
        while head and head.next:
            odd.next = ListNode(head.val)
            even.next = ListNode(head.next.val)
            odd, even, head = odd.next, even.next, head.next.next
        
        if head:
            odd.next = ListNode(head.val)
            odd = odd.next
        
        odd.next = e.next
        
        return o.next