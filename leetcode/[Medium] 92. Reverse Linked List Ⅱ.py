# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        n = new = ListNode()
        
        cnt = 1
        while cnt < left:
            new.next, head = head, head.next
            new = new.next
            cnt += 1
        
        r = None
        while cnt <= right:
            r, r.next, head = head, r, head.next
            cnt += 1
        new.next = r
        
        while new.next:
            new = new.next
        
        while head:
            new.next, head = head, head.next
            new = new.next
        
        return n.next