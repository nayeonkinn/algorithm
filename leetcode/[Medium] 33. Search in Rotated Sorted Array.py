class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right):
            if left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binarySearch(left, mid - 1)
                else:
                    return binarySearch(mid + 1, right)
            else:
                return -1

        k = len(nums) - 1
        for i in range(len(nums) - 1):
             if nums[i] > nums[i + 1]:
                k = i
                break

        if target == nums[0]:
            return 0
        elif target > nums[0]:
            return binarySearch(0, k)
        else:
            return binarySearch(k + 1, len(nums) - 1)