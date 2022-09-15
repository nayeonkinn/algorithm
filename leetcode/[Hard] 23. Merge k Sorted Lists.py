# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            while lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
    
        head = merged = ListNode()
        while heap:
            merged.next = ListNode(heappop(heap)[0])
            merged = merged.next
        return head.next