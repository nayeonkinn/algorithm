class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sortNumber(x, y):
            if str(x) + str(y) < str(y) + str(x):
                return 1
            elif str(x) + str(y) == str(y) + str(x):
                return 0
            else:
                return -1
        
        sorted_nums = sorted(nums, key = cmp_to_key(sortNumber))
        return str(int(''.join(list(map(str, sorted_nums)))))