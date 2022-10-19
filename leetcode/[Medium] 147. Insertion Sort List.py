# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = before = head
        head = head.next
        while head:
            if head.val < before.val:
                before.next = head.next
                search = before2 = answer2 = ListNode(-5001)
                search.next = answer
                search = search.next
                while search:
                    if search.val > head.val:
                        before2.next = ListNode(head.val)
                        before2.next.next = search
                        break
                    before2 = search
                    search = search.next
                answer = answer2.next
                head = search
            before = head
            head = head.next
        return answer