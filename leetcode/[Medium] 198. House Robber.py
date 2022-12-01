class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        tab = defaultdict()
        tab[0], tab[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tab[i] = max(tab[i - 1], tab[i - 2] + nums[i])
        
        return tab.popitem()[1]