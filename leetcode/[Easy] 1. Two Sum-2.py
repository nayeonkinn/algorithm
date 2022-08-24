class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, value in enumerate(nums):
            remain = target - value
            
            if remain in memo:
                return [i, memo[remain]]
            else:
                memo[value] = i