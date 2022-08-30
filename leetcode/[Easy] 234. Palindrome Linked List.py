# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        llist = [head.val]
        while head.next:
            head = head.next
            llist.append(head.val)
            
        while len(llist) >= 2:
            if llist.pop(0) != llist.pop():
                return False
        return True