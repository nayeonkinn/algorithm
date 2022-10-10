class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        
        heapq.heapify(nums)
        for _ in range(len(nums) - k + 1):
            answer = heapq.heappop(nums)
        
        return answer