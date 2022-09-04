# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        swap = ListNode()
        s = swap
        while head and head.next:
            prev, head = head.val, head.next
            swap.next = ListNode(head.val)
            swap.next.next = ListNode(prev)
            swap = swap.next.next
            head = head.next
        if head:
            swap.next = ListNode(head.val)
        return s.next