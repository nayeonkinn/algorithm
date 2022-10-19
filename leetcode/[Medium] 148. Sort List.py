# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numbers = []
        while head:
            numbers.append(head.val)
            head = head.next

        answer = root = ListNode()
        for num in sorted(numbers):
            root.next = ListNode(num)
            root = root.next

        return answer.next