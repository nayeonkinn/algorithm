class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        elif 0 in nums:
            result = [0] * len(nums)
            i = nums.index(0)
            nums.pop(i)
            result[i] = self.product(nums)
            return result
       
        else:
            val = self.product(nums)
            return [val // num for num in nums]
    
    def product(self, nums):
        result = 1
        for num in nums:
            result *= num
        return result